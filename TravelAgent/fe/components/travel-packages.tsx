import Image from "next/image"
import { Card, CardContent, CardFooter } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Star } from "lucide-react"

const packages = [
  {
    id: 1,
    title: "Japan Cherry Blossom Tour",
    image: "/placeholder.svg?height=200&width=300",
    description:
      "Experience the magic of cherry blossom season in Japan with this 10-day guided tour through Tokyo, Kyoto, and Osaka.",
    price: 2499,
    duration: "10 days",
    rating: 4.8,
    featured: true,
  },
  {
    id: 2,
    title: "European Capitals Explorer",
    image: "/placeholder.svg?height=200&width=300",
    description:
      "Visit London, Paris, Berlin, and Rome in this comprehensive 14-day tour of Europe's most iconic cities.",
    price: 2899,
    duration: "14 days",
    rating: 4.7,
    featured: false,
  },
  {
    id: 3,
    title: "Thailand Beach Retreat",
    image: "/placeholder.svg?height=200&width=300",
    description: "Relax on the pristine beaches of Phuket and Koh Samui with this 7-day luxury beach vacation package.",
    price: 1599,
    duration: "7 days",
    rating: 4.9,
    featured: true,
  },
  {
    id: 4,
    title: "New Zealand Adventure",
    image: "/placeholder.svg?height=200&width=300",
    description:
      "Explore the stunning landscapes of New Zealand with this 12-day adventure tour including hiking, kayaking, and more.",
    price: 3299,
    duration: "12 days",
    rating: 4.9,
    featured: false,
  },
]

export function TravelPackages() {
  return (
    <section className="py-12">
      <div className="flex justify-between items-center mb-8">
        <h2 className="text-3xl font-bold">Featured Travel Packages</h2>
        <Button variant="outline" className="border-teal-600 text-teal-600 hover:bg-teal-50">
          View All Packages
        </Button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {packages.map((pkg) => (
          <Card key={pkg.id} className="overflow-hidden hover:shadow-lg transition-shadow">
            <div className="relative">
              <div className="relative h-48">
                <Image src={pkg.image || "/placeholder.svg"} alt={pkg.title} fill className="object-cover" />
              </div>
              {pkg.featured && <Badge className="absolute top-2 right-2 bg-teal-600">Featured</Badge>}
            </div>
            <CardContent className="p-4">
              <div className="flex justify-between items-center mb-2">
                <h3 className="font-bold text-lg">{pkg.title}</h3>
                <div className="flex items-center">
                  <Star className="h-4 w-4 fill-yellow-400 text-yellow-400 mr-1" />
                  <span className="text-sm font-medium">{pkg.rating}</span>
                </div>
              </div>
              <p className="text-slate-600 text-sm mb-3">{pkg.description}</p>
              <div className="flex justify-between items-center text-sm text-slate-500">
                <span>{pkg.duration}</span>
                <span className="font-bold text-base text-slate-900">${pkg.price}</span>
              </div>
            </CardContent>
            <CardFooter className="p-4 pt-0">
              <Button className="w-full bg-teal-600 hover:bg-teal-700">View Details</Button>
            </CardFooter>
          </Card>
        ))}
      </div>
    </section>
  )
}
