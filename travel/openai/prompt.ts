interface Trip {
  destination: string;
  travel_start_date: string;
  travel_end_date: string;
  trip_purpose: string;
  budget: number;
  accommodation_preference: string;
  accommodation_details: string | null;
  transportation_preference: string;
  flights_booked: boolean;
  daily_itinerary: string[];
  interests: string[];
  dietary_restrictions: string[];
  travel_companions: string;
  preferred_pace: string;
  safety_health_concerns: string[];
  emergency_numbers: string[];
  language_tips: string[];
  currency_info: {
    currency: string;
    exchange_rate: number | null;
  };
  weather_forecast: any | null;
  local_sim_info: string | null;
  travel_insurance: boolean;
}
