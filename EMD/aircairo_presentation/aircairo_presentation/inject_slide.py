import html

file_path = "C:/Users/Ayman/.gemini/antigravity/scratch/aircairo_presentation/AirCairo_Seatmap_Kickoff.html"

req_xml = """<?xml version="1.0" encoding="utf-16"?>
<Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/soap/envelope/">
  <Header>
    <SecurityHeader xmlns="http://tpconnects.com/security/header">
      <agent xmlns="">WON</agent>
      <apiKey xmlns="">b5ae394d1ca7e58248e7f19b3b0d3b9a</apiKey>
      <secretKey xmlns="">037554c3-ebc7-4f24-a2c3-a84e32c37127</secretKey>
    </SecurityHeader>
  </Header>
  <Body>
    <IATA_SeatAvailRQ xmlns="http://www.iata.org/IATA/2015/00/2018.2/IATA_SeatAvailabilityRQ">
      <MessageDoc>
        <Name>NDC</Name>
        <RefVersionNumber>18.2</RefVersionNumber>
      </MessageDoc>
      <Party>
        <Participant>
          <TravelAgency>
            <AgencyID>60297</AgencyID>
            <IATANumber>90200305</IATANumber>
            <Name>Wonder Travel</Name>
            <TravelAgent>
              <TravelAgentID>60297-1853</TravelAgentID>
            </TravelAgent>
          </TravelAgency>
        </Participant>
        <Sender>
          <Aggregator>
            <AggregatorID>AGG</AggregatorID>
          </Aggregator>
          <TravelAgency>
            <AgencyID>60297</AgencyID>
            <IATANumber>90200305</IATANumber>
            <Name>Wonder Travel</Name>
            <TravelAgent>
              <TravelAgentID>60297-1853</TravelAgentID>
            </TravelAgent>
          </TravelAgency>
          <EnabledSystem>
            <SystemID>API</SystemID>
          </EnabledSystem>
        </Sender>
      </Party>
      <PayloadAttributes>
        <EchoTokenText>bc859b52-422e-4d2f-8961-c61a13263926</EchoTokenText>
        <VersionNumber>18.6</VersionNumber>
      </PayloadAttributes>
      <PointOfSale>
        <Country>
          <CountryName>Egypt</CountryName>
        </Country>
        <Device>
          <DeviceCode>::ffff:10.120.16.17</DeviceCode>
        </Device>
      </PointOfSale>
      <Request>
        <CoreRequest>
          <Offer>
            <OfferID>1H2SMZ_P0CW4GX64E1PJQUTTHD0QRZURC32</OfferID>
            <OwnerCode>SM</OwnerCode>
          </Offer>
          <PaxSegment>
            <Arrival>
              <AircraftScheduledDateTime>2026-08-17T02:05:00Z</AircraftScheduledDateTime>
              <IATALocationCode>JED</IATALocationCode>
            </Arrival>
            <CabinType>
              <CabinTypeCode>M</CabinTypeCode>
              <CabinTypeName>ECO</CabinTypeName>
            </CabinType>
            <DatedOperatingLeg>
              <IATAAircraftType>
                <IATAAircraftTypeCode>320</IATAAircraftTypeCode>
              </IATAAircraftType>
            </DatedOperatingLeg>
            <Dep>
              <AircraftScheduledDateTime>2026-08-16T23:55:00Z</AircraftScheduledDateTime>
              <IATALocationCode>CAI</IATALocationCode>
            </Dep>
            <Duration>PT2H10M</Duration>
            <MarketingCarrierInfo>
              <CarrierDesigCode>SM</CarrierDesigCode>
              <MarketingCarrierFlightNumberText>459</MarketingCarrierFlightNumberText>
            </MarketingCarrierInfo>
            <OperatingCarrierInfo>
              <CarrierDesigCode>SM</CarrierDesigCode>
            </OperatingCarrierInfo>
            <PaxSegmentID>SEG11</PaxSegmentID>
          </PaxSegment>
        </CoreRequest>
        <Pax>
          <Birthdate>1999-01-28</Birthdate>
          <Individual>
            <GivenName>Ahmed</GivenName>
            <Surname>Ali</Surname>
            <TitleName>MR</TitleName>
          </Individual>
          <PaxID>PAX1</PaxID>
          <PTC>ADT</PTC>
        </Pax>
        <ShoppingResponse>
          <ShoppingResponseID>1H2SMZ_P0CW4GX64E1PJQUTTHD0QRZURC32</ShoppingResponseID>
        </ShoppingResponse>
      </Request>
    </IATA_SeatAvailRQ>
  </Body>
</Envelope>"""

req_json = """{
    "supplier": "{{supplier}}",
    "ResponseId": "00000000-0000-0000-0000-000000000000",
    "SelectedOfferId": "{{PaxofferId}}",
    "credentialsSelector": "{{Credentials_Selector}}",
    "selectedBundles": []
}"""

res_xml = """<soap:Envelope
    xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <ns5:IATA_SeatAvailRS
            xmlns:ns2="http://www.iata.org/IATA/2015/00/2018.2/IATA_OrderRulesRQ"
            xmlns:ns3="http://www.iata.org/IATA/2015/00/2018.2/IATA_OrderRulesRS"
            xmlns:ns4="http://www.iata.org/IATA/2015/00/2018.2/IATA_SeatAvailabilityRQ"
            xmlns:ns5="http://www.iata.org/IATA/2015/00/2018.2/IATA_SeatAvailabilityRS"
            xmlns:ns6="http://www.iata.org/IATA/2015/00/2018.2/IATA_ServiceListRQ"
            xmlns:ns7="http://www.iata.org/IATA/2015/00/2018.2/IATA_ServiceListRS"
            xmlns:ns8="http://www.iata.org/IATA/2015/00/2018.2/IATA_OfferPriceRQ"
            xmlns:ns9="http://www.iata.org/IATA/2015/00/2018.2/IATA_OfferPriceRS"
            xmlns:ns10="http://tpconnects.com/security/header">
            <ns5:Response>
                <ns5:ALaCarteOffer>
                    <ns5:ALaCarteOfferItem>
                        <ns5:Eligibility>
                            <ns5:FlightAssociations>
                                <ns5:PaxSegmentRefID>SEG11</ns5:PaxSegmentRefID>
                            </ns5:FlightAssociations>
                            <ns5:PaxRefID>PAX1</ns5:PaxRefID>
                        </ns5:Eligibility>
                        <ns5:OfferItemID>SM-PRICE1-SEG11</ns5:OfferItemID>
                        <ns5:Service>
                            <ns5:ServiceDefinitionRefID>SRV1-SEG11</ns5:ServiceDefinitionRefID>
                            <ns5:ServiceID>1-SEG11</ns5:ServiceID>
                        </ns5:Service>
                        <ns5:UnitPrice>
                            <ns5:BaseAmount CurCode="EGP">1180.00</ns5:BaseAmount>
                            <ns5:TotalAmount CurCode="EGP">1180.00</ns5:TotalAmount>
                        </ns5:UnitPrice>
                    </ns5:ALaCarteOfferItem>
                    <ns5:ALaCarteOfferItem>
                        <ns5:Eligibility>
                            <ns5:FlightAssociations>
                                <ns5:PaxSegmentRefID>SEG11</ns5:PaxSegmentRefID>
                            </ns5:FlightAssociations>
                            <ns5:PaxRefID>PAX1</ns5:PaxRefID>
                        </ns5:Eligibility>
                        <ns5:OfferItemID>SM-PRICE2-SEG11</ns5:OfferItemID>
                        <ns5:Service>
                            <ns5:ServiceDefinitionRefID>SRV2-SEG11</ns5:ServiceDefinitionRefID>
                            <ns5:ServiceID>2-SEG11</ns5:ServiceID>
                        </ns5:Service>
                        <ns5:UnitPrice>
                            <ns5:BaseAmount CurCode="EGP">1180.00</ns5:BaseAmount>
                            <ns5:TotalAmount CurCode="EGP">1180.00</ns5:TotalAmount>
                        </ns5:UnitPrice>
                    </ns5:ALaCarteOfferItem>
                    <!-- Response truncated for presentation clarity -->
                    <ns5:OfferID>PRICE</ns5:OfferID>
                    <ns5:OwnerCode>SM</ns5:OwnerCode>
                </ns5:ALaCarteOffer>
                <ns5:DataLists>
                    <ns5:PaxList>
                        <ns5:Pax>
                            <ns5:PaxID>PAX1</ns5:PaxID>
                            <ns5:PTC>ADT</ns5:PTC>
                        </ns5:Pax>
                    </ns5:PaxList>
                    <ns5:PaxSegmentList>
                        <ns5:PaxSegment>
                            <ns5:Arrival>
                                <ns5:IATALocationCode>JED</ns5:IATALocationCode>
                            </ns5:Arrival>
                            <ns5:CabinType>
                                <ns5:CabinTypeCode>Y</ns5:CabinTypeCode>
                            </ns5:CabinType>
                            <ns5:Dep>
                                <ns5:IATALocationCode>CAI</ns5:IATALocationCode>
                            </ns5:Dep>
                            <ns5:PaxSegmentID>SEG11</ns5:PaxSegmentID>
                        </ns5:PaxSegment>
                    </ns5:PaxSegmentList>
                </ns5:DataLists>
                <ns5:SeatMap>
                    <ns5:CabinCompartment>
                        <ns5:CabinCompartmentID>cabin1</ns5:CabinCompartmentID>
                        <!-- Seats Data Here -->
                    </ns5:CabinCompartment>
                </ns5:SeatMap>
            </ns5:Response>
        </ns5:IATA_SeatAvailRS>
    </soap:Body>
</soap:Envelope>"""

new_slide = f"""
            <!-- Slide 3.5: API Example -->
            <section>
                <h3 class="text-blue" style="text-align: left;">API Request & Response 📡</h3>
                
                <div style="font-size: 0.45em; text-align: left; margin-top: 30px;">
                    
                    <!-- Request XML -->
                    <details class="fragment fade-up" style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #0055A5; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <summary style="font-size: 1.5em; cursor: pointer; font-weight: bold; color: #0055A5;">🔗 View Supplier Request (XML)</summary>
                        <pre style="max-height: 250px; overflow-y: auto; background: #282c34; color: #abb2bf; padding: 15px; border-radius: 8px; margin-top: 15px;"><code style="font-family: monospace;">{html.escape(req_xml)}</code></pre>
                    </details>

                    <!-- Internal JSON -->
                    <details class="fragment fade-up" style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #00A9E0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <summary style="font-size: 1.5em; cursor: pointer; font-weight: bold; color: #00A9E0;">🔗 View Internal Sent Payload (JSON)</summary>
                        <pre style="max-height: 250px; overflow-y: auto; background: #282c34; color: #abb2bf; padding: 15px; border-radius: 8px; margin-top: 15px;"><code style="font-family: monospace;">{html.escape(req_json)}</code></pre>
                    </details>

                    <!-- Response XML -->
                    <details class="fragment fade-up" style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #28a745; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <summary style="font-size: 1.5em; cursor: pointer; font-weight: bold; color: #28a745;">🔗 View Supplier Response (XML)</summary>
                        <pre style="max-height: 250px; overflow-y: auto; background: #282c34; color: #abb2bf; padding: 15px; border-radius: 8px; margin-top: 15px;"><code style="font-family: monospace;">{html.escape(res_xml)}</code></pre>
                    </details>

                </div>
            </section>
"""

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Insert right before "<!-- Slide 4: Multi-Segment Flow -->"
parts = content.split("<!-- Slide 4: Multi-Segment Flow -->")
new_content = parts[0] + new_slide + "\n            <!-- Slide 4: Multi-Segment Flow -->" + parts[1]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Added API slide.")
