import { Route, Building, Ticket, Plane } from "lucide-react"

const features = [
  {
    icon: Route,
    title: "AI-Powered Itineraries",
    description: "Personalized travel plans created just for you",
  },
  {
    icon: Building,
    title: "Accommodation",
    description: "Eco-friendly stays around the world",
  },
  {
    icon: Ticket,
    title: "Experiences",
    description: "Unforgettable activities and tours",
  },
  {
    icon: Plane,
    title: "Flights",
    description: "Carbon-offset flight options",
  },
]

export function TravelFeatures() {
  return (
    <div className="relative bg-gradient-to-b from-teal-800/90 to-teal-900">
      {/* Background image with overlay */}
      <div
        className="absolute inset-0 bg-cover bg-center z-0 opacity-20"
      ></div>

      {/* Wave decoration */}
      <div className="absolute top-0 left-0 right-0 h-24 overflow-hidden">
        <svg
          viewBox="0 0 1200 120"
          preserveAspectRatio="none"
          className="absolute bottom-0 w-full h-24 text-teal-800/90"
          fill="currentColor"
        >
          <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z"></path>
        </svg>
      </div>

      <div className="relative z-10 container mx-auto px-4 py-24">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature) => (
            <div key={feature.title} className="flex items-start">
              <div className="flex-shrink-0 mr-4">
                <div className="p-3 bg-amber-400 rounded-full">
                  <feature.icon className="h-6 w-6 text-white" />
                </div>
              </div>
              <div>
                <h3 className="text-xl font-semibold text-white mb-2">{feature.title}</h3>
                <p className="text-teal-100">{feature.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Traveler illustration */}
      <div className="absolute bottom-0 right-10 w-48 h-48 hidden lg:block">
        <div className="relative w-full h-full">
          <div className="absolute bottom-0 right-0">
            <svg width="120" height="180" viewBox="0 0 120 180" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M60 20C46.7 20 36 30.7 36 44C36 57.3 46.7 68 60 68C73.3 68 84 57.3 84 44C84 30.7 73.3 20 60 20Z"
                fill="#FFB74D"
              />
              <path d="M60 76C40.1 76 24 92.1 24 112V180H96V112C96 92.1 79.9 76 60 76Z" fill="#FF9800" />
              <path d="M84 140H96V160H84V140Z" fill="#FFB74D" />
              <rect x="72" y="160" width="24" height="20" fill="#795548" />
              <rect x="84" y="120" width="12" height="20" fill="#FFB74D" />
              <path d="M108 160H96V180H108V160Z" fill="#FFB74D" />
              <rect x="96" y="140" width="12" height="20" fill="#FF9800" />
            </svg>
          </div>
          <div className="absolute bottom-0 right-16">
            <svg width="60" height="100" viewBox="0 0 60 100" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect y="20" width="60" height="80" rx="4" fill="#78909C" />
              <rect x="10" y="30" width="40" height="60" fill="#90A4AE" />
              <rect x="20" width="20" height="20" fill="#78909C" />
            </svg>
          </div>
        </div>
      </div>
    </div>
  )
}
