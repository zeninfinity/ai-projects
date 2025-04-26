"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Card, CardContent } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Calendar } from "@/components/ui/calendar"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { format } from "date-fns"
import { CalendarIcon, Plane, Hotel, MapPin, Users } from "lucide-react"

export function TravelSearch() {
  const [date, setDate] = useState<Date | undefined>(new Date())

  return (
    <Card className="w-full max-w-4xl mx-auto shadow-lg border-teal-200 -mt-16 z-10 bg-white">
      <CardContent className="p-6">
        <Tabs defaultValue="flights" className="w-full">
          <TabsList className="grid w-full grid-cols-3 mb-6">
            <TabsTrigger value="flights" className="data-[state=active]:bg-teal-600 data-[state=active]:text-white">
              <Plane className="mr-2 h-4 w-4" />
              Flights
            </TabsTrigger>
            <TabsTrigger value="hotels" className="data-[state=active]:bg-teal-600 data-[state=active]:text-white">
              <Hotel className="mr-2 h-4 w-4" />
              Hotels
            </TabsTrigger>
            <TabsTrigger value="packages" className="data-[state=active]:bg-teal-600 data-[state=active]:text-white">
              <MapPin className="mr-2 h-4 w-4" />
              Packages
            </TabsTrigger>
          </TabsList>

          <TabsContent value="flights" className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium mb-1 block">From</label>
                <Input placeholder="Departure city" className="border-teal-200" />
              </div>
              <div>
                <label className="text-sm font-medium mb-1 block">To</label>
                <Input placeholder="Destination city" className="border-teal-200" />
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div>
                <label className="text-sm font-medium mb-1 block">Departure</label>
                <Popover>
                  <PopoverTrigger asChild>
                    <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                      <CalendarIcon className="mr-2 h-4 w-4" />
                      {date ? format(date, "PPP") : "Select date"}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0">
                    <Calendar mode="single" selected={date} onSelect={setDate} initialFocus />
                  </PopoverContent>
                </Popover>
              </div>

              <div>
                <label className="text-sm font-medium mb-1 block">Return</label>
                <Popover>
                  <PopoverTrigger asChild>
                    <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                      <CalendarIcon className="mr-2 h-4 w-4" />
                      {date ? format(date, "PPP") : "Select date"}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0">
                    <Calendar mode="single" selected={date} onSelect={setDate} initialFocus />
                  </PopoverContent>
                </Popover>
              </div>

              <div>
                <label className="text-sm font-medium mb-1 block">Passengers</label>
                <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                  <Users className="mr-2 h-4 w-4" />2 Adults, 0 Children
                </Button>
              </div>
            </div>

            <Button className="w-full bg-teal-600 hover:bg-teal-700">Search Flights</Button>
          </TabsContent>

          <TabsContent value="hotels" className="space-y-4">
            <div>
              <label className="text-sm font-medium mb-1 block">Destination</label>
              <Input placeholder="City, region, or hotel name" className="border-teal-200" />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div>
                <label className="text-sm font-medium mb-1 block">Check-in</label>
                <Popover>
                  <PopoverTrigger asChild>
                    <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                      <CalendarIcon className="mr-2 h-4 w-4" />
                      {date ? format(date, "PPP") : "Select date"}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0">
                    <Calendar mode="single" selected={date} onSelect={setDate} initialFocus />
                  </PopoverContent>
                </Popover>
              </div>

              <div>
                <label className="text-sm font-medium mb-1 block">Check-out</label>
                <Popover>
                  <PopoverTrigger asChild>
                    <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                      <CalendarIcon className="mr-2 h-4 w-4" />
                      {date ? format(date, "PPP") : "Select date"}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0">
                    <Calendar mode="single" selected={date} onSelect={setDate} initialFocus />
                  </PopoverContent>
                </Popover>
              </div>

              <div>
                <label className="text-sm font-medium mb-1 block">Guests</label>
                <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                  <Users className="mr-2 h-4 w-4" />2 Adults, 1 Room
                </Button>
              </div>
            </div>

            <Button className="w-full bg-teal-600 hover:bg-teal-700">Search Hotels</Button>
          </TabsContent>

          <TabsContent value="packages" className="space-y-4">
            <div>
              <label className="text-sm font-medium mb-1 block">Destination</label>
              <Input placeholder="Where do you want to go?" className="border-teal-200" />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label className="text-sm font-medium mb-1 block">Departure</label>
                <Popover>
                  <PopoverTrigger asChild>
                    <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                      <CalendarIcon className="mr-2 h-4 w-4" />
                      {date ? format(date, "PPP") : "Select date"}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0">
                    <Calendar mode="single" selected={date} onSelect={setDate} initialFocus />
                  </PopoverContent>
                </Popover>
              </div>

              <div>
                <label className="text-sm font-medium mb-1 block">Duration</label>
                <Button variant="outline" className="w-full justify-start text-left font-normal border-teal-200">
                  7 Days
                </Button>
              </div>
            </div>

            <Button className="w-full bg-teal-600 hover:bg-teal-700">Search Packages</Button>
          </TabsContent>
        </Tabs>
      </CardContent>
    </Card>
  )
}
