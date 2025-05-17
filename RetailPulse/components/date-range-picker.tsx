"use client"

import type * as React from "react"
import { CalendarIcon } from "lucide-react"
import { format } from "date-fns"
import { enUS } from 'date-fns/locale'
import type { DateRange } from "react-day-picker"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

interface DatePickerWithRangeProps {
  dateRange: DateRange | undefined
  setDateRange: React.Dispatch<React.SetStateAction<DateRange | undefined>>
  className?: string
}

export function DatePickerWithRange({ dateRange, setDateRange, className }: DatePickerWithRangeProps) {
  // Function to handle single date selection
  const handleSelectDate = (date: Date | undefined) => {
    if (date) {
      setDateRange({ from: date, to: date })
    } else {
      setDateRange(undefined)
    }
  }

  return (
    <div className={cn("grid gap-2", className)}>
      <style jsx global>{`
        .rdp-head {
          display: none !important;
        }
      `}</style>
      <Popover>
        <PopoverTrigger asChild>
          <Button
            id="date"
            variant={"outline"}
            className={cn("w-[300px] justify-start text-left font-normal", !dateRange && "text-muted-foreground")}
          >
            <CalendarIcon className="mr-2 h-4 w-4" />
            {dateRange?.from ? (
              dateRange.to && dateRange.from !== dateRange.to ? (
                <>
                  {format(dateRange.from, "MMM d, y", { locale: enUS })} - {format(dateRange.to, "MMM d, y", { locale: enUS })}
                </>
              ) : (
                format(dateRange.from, "MMM d, y", { locale: enUS })
              )
            ) : (
              <span>Select date</span>
            )}
          </Button>
        </PopoverTrigger>
        <PopoverContent className="w-auto p-0" align="start">
          <Tabs defaultValue="single">
            <div className="flex items-center justify-between px-4 pt-3">
              <TabsList>
                <TabsTrigger value="single">Single Date</TabsTrigger>
                <TabsTrigger value="range">Date Range</TabsTrigger>
              </TabsList>
            </div>
            <TabsContent value="single" className="p-3">
              <Calendar 
                mode="single" 
                selected={dateRange?.from} 
                onSelect={handleSelectDate} 
                initialFocus
                locale={enUS}
                weekStartsOn={1}
                showOutsideDays={false}
                modifiers={{
                  selected: (date) => dateRange?.from ? date.getTime() === dateRange.from.getTime() : false
                }}
                modifiersStyles={{
                  selected: {
                    backgroundColor: "hsl(var(--primary))",
                    color: "white",
                    fontWeight: "bold"
                  },
                  today: {
                    color: "hsl(var(--primary))",
                    fontWeight: "bold"
                  }
                }}
              />
            </TabsContent>
            <TabsContent value="range" className="p-3">
              <Calendar 
                mode="range" 
                selected={dateRange} 
                onSelect={setDateRange} 
                numberOfMonths={2} 
                initialFocus
                locale={enUS}
                weekStartsOn={1}
                showOutsideDays={false}
                modifiersStyles={{
                  selected: {
                    backgroundColor: "hsl(var(--primary))",
                    color: "white",
                    fontWeight: "bold"
                  },
                  today: {
                    color: "hsl(var(--primary))",
                    fontWeight: "bold"
                  },
                  range_start: {
                    backgroundColor: "hsl(var(--primary))",
                    color: "white",
                    fontWeight: "bold"
                  },
                  range_end: {
                    backgroundColor: "hsl(var(--primary))",
                    color: "white",
                    fontWeight: "bold"
                  },
                  range_middle: {
                    backgroundColor: "hsl(var(--accent))",
                    color: "hsl(var(--accent-foreground))"
                  }
                }}
              />
            </TabsContent>
          </Tabs>
        </PopoverContent>
      </Popover>
    </div>
  )
}
