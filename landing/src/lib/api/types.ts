export interface Service {
  id: number;
  title: string;
  description: string | null;
  price: string;
  duration: number;
  image: string | null;
  category?: string;
}

export interface ServiceCategory {
  id: number;
  name: string;
  description: string | null;
  image: string | null;
  services: Service[];
  group_id: number;
}

export interface Course {
  id: number;
  title: string;
  description: string | null;
  price: string;
  duration: number;
  image: string | null;
}

export interface AppConfig {
  company_name: string;
  brand_color: string;
  logo: string | null;
  currency: string;
  contact_email: string | null;
  contact_phone: string | null;
  event_type_label: string;
  event_label: string;
  availability_free_label: string;
  availability_regular_label: string;
  availability_no_free_label: string;
  extras_label: string;
  timezone: string;
}
