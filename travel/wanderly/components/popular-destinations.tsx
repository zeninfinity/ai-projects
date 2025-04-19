import Image from "next/image"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

const destinations = [
  {
    id: 1,
    name: "Tokyo, Japan",
    image: "/placeholder.svg?height=200&width=300",
    description: "Experience the blend of traditional culture and futuristic technology.",
    tags: ["Culture", "Food", "Shopping"],
  },
  {
    id: 2,
    name: "Paris, France",
    image: "/placeholder.svg?height=200&width=300",
    description: "Discover the city of lights with its iconic landmarks and cuisine.",
    tags: ["Romantic", "Art", "History"],
  },
  {
    id: 3,
    name: "Bali, Indonesia",
    image: "/placeholder.svg?height=200&width=300",
    description: "Relax on pristine beaches and explore lush tropical landscapes.",
    tags: ["Beach", "Nature", "Wellness"],
  },
  {
    id: 4,
    name: "New York, USA",
    image: "/placeholder.svg?height=200&width=300",
    description: "Dive into the vibrant energy of the city that never sleeps.",
    tags: ["Urban", "Entertainment", "Food"],
  },
]

export function PopularDestinations() {
  return (
    <section className="py-12">
      <h2 className="text-3xl font-bold text-center mb-8">Popular Destinations</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {destinations.map((destination) => (
          <Card key={destination.id} className="overflow-hidden hover:shadow-lg transition-shadow">
            <div className="relative h-48 bg-sky-100">
              <Image
                src={destination.image || "/placeholder.svg"}
                alt={destination.name}
                fill
                className="object-cover"
              />
            </div>
            <CardContent className="p-4">
              <h3 className="font-bold text-lg mb-2">{destination.name}</h3>
              <p className="text-slate-600 text-sm mb-3">{destination.description}</p>
              <div className="flex flex-wrap gap-2">
                {destination.tags.map((tag, index) => (
                  <Badge key={index} variant="outline" className="bg-teal-50 text-teal-700 border-teal-200">
                    {tag}
                  </Badge>
                ))}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </section>
  )
}
