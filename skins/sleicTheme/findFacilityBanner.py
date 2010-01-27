#  Script (Python) "findFacilityBanner"
#
#  Created by: Paul Rentschler
#  Description: based on the current url the script determines what 
#                if any banner should be displayed to identify the
#                facility being viewed.
#


# break the absolute url into pieces at the slash (/)
urlParts = context.absolute_url().split('/')

facility = "none"

# find the location of the "facilities" folder in the absolute url
if context.getSectionFromURL() == 'section-facilities':
  facilityPos = urlParts.index("facilities")
  if facilityPos > 0 and facilityPos < (len(urlParts) - 1):
    # facilities appears in the url somewhere and is not the last item
    facility = urlParts[facilityPos + 1]
      
    if facility == '3t-mri':
      facility = 'threet-mri'

# return the facility
return facility
