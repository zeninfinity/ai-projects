import { Button } from "@/components/ui/button"
import { Landmark, Building2, Mountain, Trees, Users, UtensilsCrossed, Music } from "lucide-react"

const categories = [
  { name: "Culture", icon: Landmark },
  { name: "City Tour", icon: Building2 },
  { name: "Adventure", icon: Mountain },
  { name: "Recreation", icon: Trees },
  { name: "Family", icon: Users },
  { name: "Culinary", icon: UtensilsCrossed },
  { name: "Nightlife", icon: Music },
]

export function TravelCategories() {
  return (
    <div className="relative py-12 bg-gradient-to-b from-teal-900/70 to-teal-800/90">
      {/* Background image with overlay */}
      <div
        className="absolute inset-0 bg-cover bg-center z-0 opacity-30"
      ></div>

      <div className="relative z-10 container mx-auto px-4">
        <div className="flex flex-wrap justify-center gap-3">
          {categories.map((category) => (
            <Button
              key={category.name}
              variant="secondary"
              className="bg-teal-600/90 hover:bg-teal-500/90 text-white border border-teal-400/30"
            >
              <category.icon className="h-4 w-4 mr-2" />
              {category.name}
            </Button>
          ))}
        </div>
      </div>
    </div>
  )
}
