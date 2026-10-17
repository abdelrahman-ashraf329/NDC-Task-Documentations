DROP TABLE  IF EXISTS `TT_TS_FB_PASSENGER_SSR_EMD`;

CREATE TABLE `TT_TS_FB_PASSENGER_SSR_EMD` (
  `ID` int NOT NULL,
  `FB_BOOKING_REF_NO` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci NOT NULL,
  `PASSENGER_NO` int NOT NULL DEFAULT '1',
  `SEGMENT_REF_NO` int NOT NULL DEFAULT '1',
  `SSR_NO` int NOT NULL DEFAULT '1',
  `LEG_NO` int NOT NULL DEFAULT '0',
  `PAX_REF_ID`        varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci          DEFAULT NULL COMMENT 'Supplier passenger key as received, e.g. T1',
  `EMD_TICKET_NUMBER` varchar(50), -- Need to confirm the size with integration
  `CONNECTED_TICKET_NUMBER` varchar(50), -- Need to confirm the size with integration
	`EMD_DETAILS`       json    DEFAULT NULL COMMENT '(ds -> description, jsc -> journeyStageCode, p -> penality)' ,
  PRIMARY KEY (`ID`,`FB_BOOKING_REF_NO`,`PASSENGER_NO`,`SSR_NO`,`LEG_NO`),
  UNIQUE KEY `TT_TS_FB_PASSENGER_SSR_UK` (`FB_BOOKING_REF_NO`,`PASSENGER_NO`,`SEGMENT_REF_NO`,`SSR_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
