import html
import codecs

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
      <Request>
        <CoreRequest>
          <PaxSegment>
            <Arrival>
              <IATALocationCode>JED</IATALocationCode>
            </Arrival>
            <Dep>
              <IATALocationCode>CAI</IATALocationCode>
            </Dep>
            <PaxSegmentID>SEG11</PaxSegmentID>
          </PaxSegment>
        </CoreRequest>
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

res_xml = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <ns5:IATA_SeatAvailRS xmlns:ns5="...">
            <ns5:Response>
                <ns5:ALaCarteOffer>
                    <ns5:ALaCarteOfferItem>
                        <ns5:OfferItemID>SM-PRICE1-SEG11</ns5:OfferItemID>
                        <ns5:UnitPrice>
                            <ns5:TotalAmount CurCode="EGP">1180.00</ns5:TotalAmount>
                        </ns5:UnitPrice>
                    </ns5:ALaCarteOfferItem>
                </ns5:ALaCarteOffer>
                <ns5:SeatMap>
                    <ns5:CabinCompartment>
                        <!-- Seat Map Layout Data -->
                        <ns5:SeatRow>
                            <ns5:RowNumber>1</ns5:RowNumber>
                            <ns5:Seat>
                                <ns5:ColumnID>A</ns5:ColumnID>
                                <ns5:OccupationStatusCode>F</ns5:OccupationStatusCode>
                                <ns5:OfferItemRefID>SM-PRICE1-SEG11</ns5:OfferItemRefID>
                            </ns5:Seat>
                        </ns5:SeatRow>
                    </ns5:CabinCompartment>
                </ns5:SeatMap>
            </ns5:Response>
        </ns5:IATA_SeatAvailRS>
    </soap:Body>
</soap:Envelope>"""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Air Cairo Seat Map Integration - Kick-off</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reset.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/theme/simple.min.css" id="theme">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&family=Poppins:wght@400;600&family=Cairo:wght@400;700&display=swap" rel="stylesheet">

    <style>
        .reveal {{
            font-family: 'Poppins', sans-serif;
            color: #333;
        }}
        .reveal h1, .reveal h2, .reveal h3, .reveal h4, .reveal h5, .reveal h6 {{
            font-family: 'Montserrat', sans-serif;
            text-transform: none;
        }}
        
        /* Air Cairo Branding */
        .bg-blue {{ background-color: #0055A5 !important; color: white !important; }}
        .bg-blue h1, .bg-blue h2, .bg-blue h3, .bg-blue h4, .bg-blue p {{ color: white !important; }}
        .text-blue {{ color: #0055A5 !important; }}
        .text-lightblue {{ color: #00A9E0 !important; }}
        .text-orange {{ color: #FF9900 !important; }}
        
        /* Utility Classes */
        .box {{
            background-color: #f8f9fa;
            border-radius: 12px;
            padding: 25px;
            border-left: 5px solid #00A9E0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-top: 20px;
        }}
        
        /* Flow & Timeline styles */
        .airport-badge {{
            background: #0055A5;
            color: white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            font-family: 'Montserrat';
        }}
        .flow-box {{
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            width: 200px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }}
        .flow-box h4 {{ margin: 0 0 10px 0; color: #0055A5; font-size: 1.1em; border-bottom: 1px solid #eee; padding-bottom: 5px;}}
        .action-btn {{
            background: #f4f4f4;
            padding: 8px;
            border-radius: 5px;
            font-size: 0.6em;
            font-weight: 600;
            border: 1px solid #ccc;
        }}
        .action-btn.success {{
            background: #28a745;
            color: white;
            border-color: #218838;
        }}
        .arrow-down {{ font-size: 1.2em; color: #999; margin: 5px 0; }}
        
        /* Boarding Pass Style for Example */
        .boarding-pass {{
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border: 1px solid #ddd;
        }}
        .bp-header {{
            background: #0055A5;
            color: white;
            padding: 10px 20px;
            font-weight: bold;
            font-size: 1em;
            font-family: 'Montserrat';
        }}
        .bp-body {{
            padding: 20px;
            font-size: 0.9em;
            line-height: 1.6;
        }}
        .bp-body hr {{ border: none; border-top: 1px dashed #ccc; margin: 15px 0; }}
        
        /* Timeline */
        .tl-item {{
            background: white;
            border: 2px solid #ccc;
            padding: 10px;
            border-radius: 8px;
            display: inline-block;
            font-weight: 600;
            min-width: 180px;
            text-align: center;
        }}
        .tl-item.highlight {{ border-color: #00A9E0; background: #f0fbff; color: #0055A5; }}
        .tl-item.success {{ border-color: #28a745; background: #eafbee; color: #15803d; }}
        .tl-arrow {{
            text-align: center;
            color: #999;
            font-size: 1.2em;
            margin: 5px 0;
        }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">

            <!-- Slide 1: Title -->
            <section data-background-color="#0055A5" class="bg-blue">
                <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; height: 100%;">
                    <h2 style="font-weight: 800; font-size: 2em; margin-bottom: 10px;">Air Cairo Seat Map Integration</h2>
                    <h3 style="color: #00A9E0 !important; font-weight: 600; letter-spacing: 2px;">KICK-OFF</h3>
                    
                    <div style="width: 80px; height: 4px; background-color: #FF9900; margin: 30px 0;"></div>
                    
                    <h4 style="font-weight: normal; font-size: 1.1em; opacity: 0.9;">Seat Availability & Seat Selection Integration</h4>
                    
                    <div style="margin-top: 50px; text-align: left; background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; border-left: 4px solid #FF9900; min-width: 350px;">
                        <p style="margin: 0; font-size: 0.7em; font-family: 'Montserrat';"><strong style="opacity: 0.7;">Presented by:</strong><br><span style="font-size: 1.3em;">Ayman Mohamed</span></p>
                        <p style="margin: 15px 0 0 0; font-size: 0.7em; font-family: 'Montserrat';"><strong style="opacity: 0.7;">Date:</strong><br><span style="font-size: 1.3em;">September 2026</span></p>
                    </div>
                </div>
            </section>

            <!-- Slide 2: Objective -->
            <section>
                <h3 class="text-blue" style="text-align: left;">Objective 🎯</h3>
                <div class="box" style="text-align: left; font-size: 0.75em;">
                    <ul style="line-height: 2;">
                        <li class="fragment fade-up">Integrate <strong>Air Cairo Seat Map</strong> functionality into the NDC supplier integration.</li>
                        <li class="fragment fade-up">Retrieve <strong>available seats</strong> for each flight segment.</li>
                        <li class="fragment fade-up">Support <strong>seat selection</strong> for eligible passengers.</li>
                        <li class="fragment fade-up">Handle seat <strong>prices and characteristics</strong> correctly.</li>
                        <li class="fragment fade-up">Ensure the selected seats are <strong>correctly passed during booking</strong>.</li>
                    </ul>
                </div>
            </section>

            <!-- Slide 3: Business Rules -->
            <section>
                <h3 class="text-blue" style="text-align: left;">Business Rules 📋</h3>
                <div style="display: flex; gap: 30px; margin-top: 30px; align-items: stretch;">
                    <!-- Left Column: Passengers -->
                    <div style="flex: 1; text-align: left; font-size: 0.7em;">
                        <div class="fragment fade-right" style="background: #f0f7f4; border-left: 5px solid #28a745; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                            <div style="color: #28a745; font-weight: bold; font-size: 1.2em; margin-bottom: 5px;">ADT & CHD</div>
                            Supported ✔️
                        </div>
                        <div class="fragment fade-right" data-fragment-index="1" style="background: #fff0f0; border-left: 5px solid #dc3545; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                            <div style="color: #dc3545; font-weight: bold; font-size: 1.2em; margin-bottom: 5px;">INF</div>
                            Seat selection is <strong>not supported</strong> ❌
                        </div>
                    </div>
                    <!-- Right Column: Logic -->
                    <div style="flex: 2; text-align: left; font-size: 0.65em; background: white; padding: 25px; border-radius: 12px; border: 1px solid #eaeaea; box-shadow: 0 8px 15px rgba(0,0,0,0.05);">
                        <ul style="line-height: 1.8; margin-left: 20px;">
                            <li class="fragment fade-up" data-fragment-index="2">Seat Map is supported for <strong>all flights</strong>.</li>
                            <li class="fragment fade-up" data-fragment-index="2">Seat availability must be requested <strong>per flight segment</strong>.</li>
                            <li class="fragment fade-up" data-fragment-index="3">For connecting flights, a separate Seat Availability request is required for <strong>each segment</strong>.</li>
                            <li class="fragment fade-up" data-fragment-index="4">Available/vacant seats are provided in the Seat Availability response.</li>
                            <li class="fragment fade-up" data-fragment-index="4">Seat selection should be based on the returned availability.</li>
                            <li class="fragment fade-up" data-fragment-index="5"><strong>No gender-specific</strong> seat restrictions provided by Air Cairo (Male/Female).</li>
                        </ul>
                        <div class="fragment fade-up" data-fragment-index="6" style="margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px; font-size: 0.9em; color: #666; border-left: 3px solid #ccc;">
                            <em>Note: No additional airline-specific rules were provided by Air Cairo.</em>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Slide 3.5: API Example -->
            <section>
                <h3 class="text-blue" style="text-align: left;">API Request & Response 📡</h3>
                
                <div style="font-size: 0.45em; text-align: left; margin-top: 30px;">
                    
                    <details class="fragment fade-up" style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #0055A5; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <summary style="font-size: 1.5em; cursor: pointer; font-weight: bold; color: #0055A5;">🔗 View Supplier Request (XML)</summary>
                        <pre style="max-height: 250px; overflow-y: auto; background: #282c34; color: #abb2bf; padding: 15px; border-radius: 8px; margin-top: 15px;"><code style="font-family: monospace;">{html.escape(req_xml)}</code></pre>
                    </details>

                    <details class="fragment fade-up" style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #00A9E0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <summary style="font-size: 1.5em; cursor: pointer; font-weight: bold; color: #00A9E0;">🔗 View Internal Sent Payload (JSON)</summary>
                        <pre style="max-height: 250px; overflow-y: auto; background: #282c34; color: #abb2bf; padding: 15px; border-radius: 8px; margin-top: 15px;"><code style="font-family: monospace;">{html.escape(req_json)}</code></pre>
                    </details>

                    <details class="fragment fade-up" style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #28a745; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <summary style="font-size: 1.5em; cursor: pointer; font-weight: bold; color: #28a745;">🔗 View Supplier Response (XML)</summary>
                        <pre style="max-height: 250px; overflow-y: auto; background: #282c34; color: #abb2bf; padding: 15px; border-radius: 8px; margin-top: 15px;"><code style="font-family: monospace;">{html.escape(res_xml)}</code></pre>
                    </details>
                    
                    <details class="fragment fade-up" style="background: white; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #FF9900; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                        <summary style="font-size: 1.5em; cursor: pointer; font-weight: bold; color: #FF9900;">🔗 View Seat Map Visualization (Interactive GUI)</summary>
                        <div style="margin-top: 15px; background: #fafafa; border: 1px solid #ddd; padding: 20px; border-radius: 8px; max-height: 400px; overflow-y: auto;">
                            <h2 class="sr-only" style="display:none;">خريطة مقاعد الطائرة مع تلوين كل فئة سعر بلون مختلف</h2>
                            <div style="display:flex;flex-direction:column;align-items:center;gap:4px;padding:1rem 0;direction:rtl">
                            <div style="font-size:12px;color:#888;">دورة مياه + مطبخ</div>
                            <div id="seatmap" style="display:flex;flex-direction:column;gap:2px;font-family:Arial,sans-serif;"></div>
                            <div style="font-size:12px;color:#888;margin-top:4px">دورة مياه</div>
                            <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:14px;font-size:12px;justify-content:center;" id="legend"></div>
                            </div>
                            <script>
                            (function(){{
                                const cell = 30, gap = 2;
                                const tiers = {{
                                p1: {{bg:'#FAC775', fg:'#412402', label:'1180 ج.م - صف أول (مساحة أرجل)'}},
                                win: {{bg:'#B5D4F4', fg:'#042C53', label:'614 ج.م - شباك'}},
                                aisle: {{bg:'#9FE1CB', fg:'#04342C', label:'614 ج.م - ممر'}},
                                mid: {{bg:'#CECBF6', fg:'#26215C', label:'236 ج.م - وسط'}}
                                }};
                                function rowFull(n){{
                                return {{A:n===1?'p1':'win', B:n===1?'p1':'mid', C:n===1?'p1':'aisle', D:n===1?'p1':'aisle', E:n===1?'p1':'mid', F:n===1?'p1':'win'}};
                                }}
                                function row2(){{ return {{A:null,B:'mid',C:null,D:'aisle',E:'mid',F:null}}; }}
                                function row345(){{ return {{A:null,B:'mid',C:'aisle',D:'aisle',E:'mid',F:null}}; }}
                                function rowEmpty(){{ return {{A:null,B:null,C:null,D:null,E:null,F:null}}; }}
                                const rows = [];
                                for(let n=1;n<=30;n++){{
                                if(n===1) rows.push([n, rowFull(n)]);
                                else if(n===2) rows.push([n, row2()]);
                                else if(n>=3&&n<=5) rows.push([n, row345()]);
                                else if(n===12||n===13) rows.push([n, rowEmpty()]);
                                else rows.push([n, rowFull(n)]);
                                }}
                                setTimeout(() => {{
                                    const map = document.getElementById('seatmap');
                                    const legend = document.getElementById('legend');
                                    if(!map || map.innerHTML !== "") return;
                                    const header = document.createElement('div');
                                    header.style.cssText = 'display:flex;gap:'+gap+'px;font-size:11px;color:#888;margin-bottom:2px';
                                    header.innerHTML = '<div style="width:22px"></div>' + ['A','B','C'].map(c=>`<div style="width:`+cell+`px;text-align:center">`+c+`</div>`).join('') + '<div style="width:12px"></div>' + ['D','E','F'].map(c=>`<div style="width:`+cell+`px;text-align:center">`+c+`</div>`).join('');
                                    map.appendChild(header);
                                    rows.forEach(([n, seats])=>{{
                                    const r = document.createElement('div');
                                    r.style.cssText = 'display:flex;gap:'+gap+'px;align-items:center';
                                    let html = `<div style="width:22px;font-size:11px;color:#888;text-align:center">`+n+`</div>`;
                                    ['A','B','C'].forEach(c=>{{
                                        const t = seats[c];
                                        html += t ? `<div style="width:`+cell+`px;height:`+cell+`px;border-radius:4px;background:`+tiers[t].bg+`;color:`+tiers[t].fg+`;font-size:10px;display:flex;align-items:center;justify-content:center;font-weight:bold;">`+c+`</div>` : `<div style="width:`+cell+`px;height:`+cell+`px"></div>`;
                                    }});
                                    html += `<div style="width:12px"></div>`;
                                    ['D','E','F'].forEach(c=>{{
                                        const t = seats[c];
                                        html += t ? `<div style="width:`+cell+`px;height:`+cell+`px;border-radius:4px;background:`+tiers[t].bg+`;color:`+tiers[t].fg+`;font-size:10px;display:flex;align-items:center;justify-content:center;font-weight:bold;">`+c+`</div>` : `<div style="width:`+cell+`px;height:`+cell+`px"></div>`;
                                    }});
                                    r.innerHTML = html;
                                    map.appendChild(r);
                                    }});
                                    Object.values(tiers).forEach(t=>{{
                                    const item = document.createElement('div');
                                    item.style.cssText = 'display:flex;align-items:center;gap:6px';
                                    item.innerHTML = `<span style="width:14px;height:14px;border-radius:4px;background:`+t.bg+`;display:inline-block"></span><span style="color:#555;font-size:1.3em;font-family:Cairo,sans-serif;">`+t.label+`</span>`;
                                    legend.appendChild(item);
                                    }});
                                }}, 800);
                            }})();
                            </script>
                        </div>
                    </details>
                </div>
            </section>

            <!-- Slide 4: Multi-Segment Flow -->
            <section>
                <h3 class="text-blue" style="text-align: left;">Seat Availability Flow ✈️</h3>
                
                <div style="display: flex; justify-content: center; align-items: center; gap: 30px; margin-top: 30px;" class="fragment fade-down">
                    <div class="airport-badge">CAI</div>
                    <div style="font-size: 1.8em; color: #00A9E0;">&#10132;</div>
                    <div class="airport-badge">JED</div>
                    <div style="font-size: 1.8em; color: #00A9E0;">&#10132;</div>
                    <div class="airport-badge">RUH</div>
                </div>
                
                <div style="display: flex; justify-content: center; gap: 60px; margin-top: 40px;">
                    <div class="flow-box fragment fade-up">
                        <h4>Segment 1</h4>
                        <div class="arrow-down">⬇</div>
                        <div class="action-btn">Seat Availability</div>
                        <div class="arrow-down">⬇</div>
                        <div class="action-btn success">Select Seat</div>
                    </div>
                    
                    <div class="flow-box fragment fade-up" data-fragment-index="1">
                        <h4>Segment 2</h4>
                        <div class="arrow-down">⬇</div>
                        <div class="action-btn">Seat Availability</div>
                        <div class="arrow-down">⬇</div>
                        <div class="action-btn success">Select Seat</div>
                    </div>
                </div>

                <div class="fragment fade-up" data-fragment-index="2" style="margin: 40px auto 0 auto; max-width: 600px; background: rgba(255, 153, 0, 0.1); padding: 15px 25px; border-radius: 8px; border-left: 5px solid #FF9900; text-align: left; font-size: 0.7em;">
                    <strong style="color: #d98200; font-size: 1.2em;">🔑 Key Rule:</strong><br>
                    One Seat Availability call per segment.
                </div>
            </section>

            <!-- Slide 5: Seat Information -->
            <section>
                <h3 class="text-blue" style="text-align: left;">Seat Data to Handle 💺</h3>
                <div style="display: flex; gap: 30px; margin-top: 30px; align-items: center;">
                    <div style="flex: 1.5; text-align: left; font-size: 0.7em;">
                        <p style="color: #666; margin-bottom: 20px;">For each available seat, we need to process:</p>
                        <ul style="line-height: 1.7; margin-left: 20px;">
                            <li class="fragment fade-up">Seat / Cell ID</li>
                            <li class="fragment fade-up">Segment reference</li>
                            <li class="fragment fade-up">Cabin</li>
                            <li class="fragment fade-up">Seat characteristics</li>
                            <li class="fragment fade-up">Availability status</li>
                            <li class="fragment fade-up">Seat price & Currency</li>
                            <li class="fragment fade-up">Passenger eligibility</li>
                            <li class="fragment fade-up">Chargeable / Free seat</li>
                        </ul>
                    </div>
                    <div style="flex: 1;" class="fragment fade-left">
                        <div class="boarding-pass">
                            <div class="bp-header">📝 Example Data</div>
                            <div class="bp-body" style="text-align: left;">
                                <p><strong>Seat:</strong> 12A <span style="float:right; background: #28a745; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;">Available</span></p>
                                <p><strong>Segment:</strong> SEG1</p>
                                <p><strong>Cabin:</strong> Economy</p>
                                <hr>
                                <p style="font-size: 1.4em; text-align: center; color: #0055A5; margin: 10px 0;"><strong>Price:</strong> 500 EGP</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Slide 6: Scope -->
            <section>
                <h3 class="text-blue" style="text-align: left;">Scope 🎯</h3>
                <div style="display: flex; gap: 25px; margin-top: 30px; align-items: stretch;">
                    <!-- In Scope -->
                    <div class="fragment fade-up" style="flex: 1; text-align: left; background: white; border-top: 6px solid #28a745; padding: 25px; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.08);">
                        <h4 style="color: #28a745; margin-bottom: 20px; font-size: 1.2em; display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 1.2em;">✔️</span> In Scope
                        </h4>
                        <ul style="font-size: 0.6em; line-height: 1.7; margin-left: 20px; color: #444;">
                            <li>Air Cairo Seat Availability integration</li>
                            <li>Segment-level seat availability</li>
                            <li>ADT & CHD seat selection</li>
                            <li>Seat characteristics mapping</li>
                            <li>Seat price mapping</li>
                            <li>Free and chargeable seats</li>
                            <li>Multi-segment / connecting flights</li>
                            <li>Seat selection during booking</li>
                            <li>Validation of selected seats</li>
                        </ul>
                    </div>
                    <!-- Out of Scope -->
                    <div class="fragment fade-up" data-fragment-index="1" style="flex: 1; text-align: left; background: white; border-top: 6px solid #dc3545; padding: 25px; border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.08);">
                        <h4 style="color: #dc3545; margin-bottom: 20px; font-size: 1.2em; display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 1.2em;">❌</span> Out of Scope
                        </h4>
                        <ul style="font-size: 0.6em; line-height: 1.7; margin-left: 20px; color: #444;">
                            <li>INF seat selection</li>
                            <li>Airline-specific rules not provided by Air Cairo</li>
                            <li>Any functionality outside the Seat Map flow</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Slide 7: Implementation Plan -->
            <section>
                <h3 class="text-blue" style="text-align: left;">Implementation Phases 🛠️</h3>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-top: 30px;">
                    <!-- Phase 1 -->
                    <div class="fragment fade-up" style="text-align: left; background: white; padding: 20px; border-radius: 12px; border-left: 5px solid #0055A5; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                        <h4 style="color: #0055A5; font-size: 0.9em; margin-bottom: 12px; font-weight: bold;">1. Investigation</h4>
                        <ul style="font-size: 0.55em; line-height: 1.6; margin-left: 15px; color: #555;">
                            <li>Review Air Cairo Seat Availability doc.</li>
                            <li>Analyze existing supplier implementation.</li>
                            <li>Validate request/response structure.</li>
                            <li>Identify required metadata.</li>
                        </ul>
                    </div>
                    <!-- Phase 2 -->
                    <div class="fragment fade-up" data-fragment-index="1" style="text-align: left; background: white; padding: 20px; border-radius: 12px; border-left: 5px solid #00A9E0; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                        <h4 style="color: #00A9E0; font-size: 0.9em; margin-bottom: 12px; font-weight: bold;">2. Project Run</h4>
                        <ul style="font-size: 0.55em; line-height: 1.6; margin-left: 15px; color: #555;">
                            <li>Prepare integration flow.</li>
                            <li>Configure required supplier services.</li>
                            <li>Prepare test scenarios.</li>
                        </ul>
                    </div>
                    <!-- Phase 3 -->
                    <div class="fragment fade-up" data-fragment-index="2" style="text-align: left; background: white; padding: 20px; border-radius: 12px; border-left: 5px solid #FF9900; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                        <h4 style="color: #FF9900; font-size: 0.9em; margin-bottom: 12px; font-weight: bold;">3. Implementation</h4>
                        <ul style="font-size: 0.55em; line-height: 1.6; margin-left: 15px; color: #555;">
                            <li>Build Seat Availability request.</li>
                            <li>Implement response mapping.</li>
                            <li>Implement characteristics & pricing.</li>
                            <li>Segment-level & passenger processing.</li>
                        </ul>
                    </div>
                    <!-- Phase 4 -->
                    <div class="fragment fade-up" data-fragment-index="3" style="text-align: left; background: white; padding: 20px; border-radius: 12px; border-left: 5px solid #28a745; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                        <h4 style="color: #28a745; font-size: 0.9em; margin-bottom: 12px; font-weight: bold;">4. Testing</h4>
                        <ul style="font-size: 0.55em; line-height: 1.6; margin-left: 15px; color: #555;">
                            <li>ADT/CHD, Single/Connecting flights.</li>
                            <li>Free/Chargeable seats & features.</li>
                            <li>INF restriction validation.</li>
                            <li>Booking with selected seats.</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Slide 8: Booking Flow -->
            <section>
                <h3 class="text-blue" style="text-align: left;">Booking Flow & Services 🛒</h3>
                
                <div style="display: flex; gap: 40px; margin-top: 30px; align-items: center;">
                    <div class="fragment fade-right" style="flex: 1; text-align: center; font-size: 0.6em; display: flex; flex-direction: column; justify-content: center; background: #f8f9fa; border-radius: 12px; padding: 30px; border: 1px solid #ddd;">
                        <div class="tl-item">AirShopping</div>
                        <div class="tl-arrow">⬇</div>
                        <div class="tl-item">OfferPrice</div>
                        <div class="tl-arrow">⬇</div>
                        <div class="tl-item" style="background: #0055A5; color: white; padding: 15px; border: none; box-shadow: 0 5px 15px rgba(0,85,165,0.3);">
                            <strong style="font-size: 1.2em; display: block; margin-bottom: 5px;">Optional Services</strong>
                            <div style="font-size: 0.8em; opacity: 0.9; font-weight: normal; background: rgba(0,0,0,0.2); padding: 5px; border-radius: 5px; margin-top: 5px;">
                                No Ancillary / No Seat<br>
                                Ancillary Only<br>
                                Seat Only<br>
                                Ancillary + Seat
                            </div>
                        </div>
                        <div class="tl-arrow">⬇</div>
                        <div class="tl-item success">OrderCreate / Booking</div>
                    </div>
                    
                    <div class="fragment fade-left" style="flex: 1.5; text-align: left; font-size: 0.65em;">
                        <h4 style="color: #0055A5; margin-bottom: 20px; font-size: 1.1em;">Possible Booking Scenarios:</h4>
                        
                        <div class="fragment fade-up" data-fragment-index="1" style="background: white; border-left: 5px solid #999; padding: 15px; margin-bottom: 12px; border-radius: 0 8px 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                            <strong style="color: #666; font-size: 1.1em;">📦 Basic Booking:</strong><br>
                            <span style="color: #555;">No Seat + No Ancillary</span>
                        </div>
                        
                        <div class="fragment fade-up" data-fragment-index="2" style="background: white; border-left: 5px solid #FF9900; padding: 15px; margin-bottom: 12px; border-radius: 0 8px 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                            <strong style="color: #d98200; font-size: 1.1em;">🍔 Ancillary Only:</strong><br>
                            <span style="color: #555;">Baggage / Meal / Other Ancillary</span>
                        </div>
                        
                        <div class="fragment fade-up" data-fragment-index="3" style="background: white; border-left: 5px solid #00A9E0; padding: 15px; margin-bottom: 12px; border-radius: 0 8px 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                            <strong style="color: #007ba3; font-size: 1.1em;">💺 Seat Only:</strong><br>
                            <span style="color: #555;">Seat Selection without Ancillaries</span>
                        </div>
                        
                        <div class="fragment fade-up" data-fragment-index="4" style="background: white; border-left: 5px solid #28a745; padding: 15px; border-radius: 0 8px 8px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                            <strong style="color: #15803d; font-size: 1.1em;">⭐ Seat + Ancillary:</strong><br>
                            <span style="color: #555;">Seat Selection combined with Ancillaries</span>
                        </div>
                    </div>
                </div>
            </section>

        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.3.1/reveal.min.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            transition: 'slide',
            autoAnimateEasing: 'ease-out',
            autoAnimateDuration: 0.8,
            autoAnimateUnmatched: false
        }});
    </script>
</body>
</html>"""

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(full_html)

print("File successfully recreated with pure UTF-8 encoding!")
