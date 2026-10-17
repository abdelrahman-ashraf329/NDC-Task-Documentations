-- Write your SQL here
DROP PROCEDURE IF EXISTS `GET_ANCILLARY_DETAILS`;

DELIMITER $$
CREATE DEFINER=`root`@`%` PROCEDURE `GET_ANCILLARY_DETAILS`(
    IN BOOKING_REF VARCHAR(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_unicode_ci
)
BEGIN
    DROP TEMPORARY TABLE IF EXISTS RESULT_01;
    CREATE TEMPORARY TABLE RESULT_01 AS
SELECT
    pd.FIRST_NAME       AS 'passengerFirstName',
    pd.LAST_NAME       AS 'passengerLastName',
    pd.PASSENGER_TYPE   AS 'passengerType',
    sd.ORIGIN           AS 'segmentOrigin',
    sd.DESTINATION      AS 'segmentDestination',
    ld.ORIGIN           AS 'legOrigin',
    ld.DESTINATION      AS 'legDestination',
    pssr.SSR_TYPE       AS 'ssrType',
    pssr.SSR_CODE       AS 'ssrCode',
    se.EMD_TICKET_NUMBER AS 'emdTicketNumber',
    se.CONNECTED_TICKET_NUMBER AS 'connectedTicketNumber',
    pssr.DESCRIPTION    AS 'ssrDescription',
    pssr.LEG_NO         AS 'legNumber',
    pssr.SEGMENT_REF_NO AS 'segmentNumber',
    pssr.PASSENGER_NO   AS 'passengerNumber',
    pssr.SSR_AMOUNT     AS 'price',
    pssr.CURRENCY       AS 'currency'
FROM TT_TS_FB_PASSENGER_SSR pssr
         INNER JOIN TT_TS_FB_PASSENGER_DETAIL pd
                    ON pd.FB_BOOKING_REF_NO = pssr.FB_BOOKING_REF_NO
                        AND pd.PASSENGER_NO = pssr.PASSENGER_NO
         INNER JOIN TT_TS_FB_SEGMENT_DETAIL sd
                    ON sd.FB_BOOKING_REF_NO = pssr.FB_BOOKING_REF_NO
                        AND sd.SEGMENT_NO = pssr.SEGMENT_REF_NO
         INNER JOIN TT_TS_FB_FLIGHTS_LEG_DETAIL ld
                    ON ld.FB_BOOKING_REF_NO = pssr.FB_BOOKING_REF_NO
                        AND ld.SEGMENT_REF_NO = pssr.SEGMENT_REF_NO
                        AND ld.LEG_ORDER = pssr.LEG_NO
         -- LEFT JOIN: most SSRs have no EMD (non NDC suppliers, bundles, older bookings) and must still be returned.
         -- An SSR returns one row per EMD - e.g. journey level baggage has one EMD per leg.
         LEFT JOIN TT_TS_FB_PASSENGER_SSR_EMD se
                    ON se.FB_BOOKING_REF_NO = pssr.FB_BOOKING_REF_NO
                        AND se.PASSENGER_NO = pssr.PASSENGER_NO
                        AND se.SSR_NO = pssr.SSR_NO
WHERE pssr.FB_BOOKING_REF_NO = BOOKING_REF;

SELECT * FROM RESULT_01;
END$$

DELIMITER ;

-- Put your rollback script here *COMMENTED*, or safely delete this comment if there isn't one
-- DROP PROCEDURE IF EXISTS GET_ANCILLARY_DETAILS;