create table public.testimonials (
  id uuid primary key default gen_random_uuid(),
  display_name text not null check (char_length(btrim(display_name)) between 2 and 100),
  organization_name text check (organization_name is null or char_length(btrim(organization_name)) <= 120),
  project_name text check (project_name is null or char_length(btrim(project_name)) <= 160),
  quote text not null check (char_length(btrim(quote)) between 20 and 1200),
  display_consent boolean not null default false,
  status text not null default 'pending' check (status in ('pending', 'approved', 'rejected')),
  approved_at timestamptz,
  approved_by uuid references public.profiles(id) on delete set null,
  created_at timestamptz not null default now(),
  constraint testimonials_approval_fields_check check (
    (status = 'approved' and approved_at is not null and approved_by is not null)
    or (status in ('pending', 'rejected') and approved_at is null and approved_by is null)
  )
);

create index testimonials_status_created_at_idx on public.testimonials(status, created_at desc);
alter table public.testimonials enable row level security;
grant select, insert, update on public.testimonials to anon, authenticated;

create policy "Anyone may submit Elyra feedback for review"
on public.testimonials for insert to anon, authenticated
with check (
  status = 'pending'
  and display_consent = true
  and approved_at is null
  and approved_by is null
);

create policy "Public may read approved Elyra feedback"
on public.testimonials for select to anon, authenticated
using (status = 'approved' and display_consent = true);

create policy "Elyra administrators may read all feedback"
on public.testimonials for select to authenticated
using (app_private.is_admin());

create policy "Elyra administrators may moderate feedback"
on public.testimonials for update to authenticated
using (app_private.is_admin())
with check (app_private.is_admin());
