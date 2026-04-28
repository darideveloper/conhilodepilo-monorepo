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
