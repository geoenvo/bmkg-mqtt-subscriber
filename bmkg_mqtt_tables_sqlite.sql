--
-- File generated with SQLiteStudio v3.1.1 on Thu Jan 11 18:39:08 2018
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: digital_forecast
CREATE TABLE digital_forecast (
    pk                  INTEGER         PRIMARY KEY AUTOINCREMENT
                                        ,
    batch_time          TIMESTAMP       
                                        DEFAULT (CURRENT_TIMESTAMP),
    bps_id              VARCHAR (100),
    domain              VARCHAR (50)    ,
    timestamp           DATETIME        ,
    area_id             INTEGER (10),
    area_latitude       DECIMAL (10, 6),
    area_longitude      DECIMAL (10, 6),
    area_coordinate     VARCHAR (200),
    area_type           VARCHAR (50),
    area_level          INTEGER (20),
    area_name_id        VARCHAR (100),
    area_name_en        VARCHAR (100),
    area_description    VARCHAR (100),
    area_domain         VARCHAR (50),
    area_tags           VARCHAR (100),
    heatindex_id               VARCHAR (50),
    heatindex_description      VARCHAR (100),
    heatindex_type             VARCHAR (100),
    heatindex_00               DECIMAL (10, 0),
    heatindex_00_hour          INTEGER (10),
    heatindex_06               DECIMAL (10, 0),
    heatindex_06_hour          INTEGER (10),
    heatindex_12_hour          INTEGER (10),
    heatindex_12               DECIMAL (10, 6),
    heatindex_18_hour          INTEGER (10),
    heatindex_18               DECIMAL (10, 6),
    heatindex_24_hour          INTEGER (10),
    heatindex_24               DECIMAL (10, 6),
    heatindex_30_hour          INTEGER (10),
    heatindex_30               DECIMAL (10, 6),
    heatindex_36_hour          INTEGER (10),
    heatindex_36               DECIMAL (10, 6),
    heatindex_42_hour          INTEGER (10),
    heatindex_42               DECIMAL (10, 6),
    heatindex_48_hour          INTEGER (10),
    heatindex_48               DECIMAL (10, 6),
    heatindex_54_hour          INTEGER (10),
    heatindex_54               DECIMAL (10, 6),
    heatindex_60_hour          INTEGER (10),
    heatindex_60               DECIMAL (10, 6),
    heatindex_66_hour          INTEGER (10),
    heatindex_66               DECIMAL (10, 6),
    heatindex_72_hour          INTEGER (10),
    heatindex_72               DECIMAL (10, 6),
    heatindex_78_hour          INTEGER (10),
    heatindex_78               DECIMAL (10, 6),
    hu_id               VARCHAR (50),
    hu_description      VARCHAR (100),
    hu_type             VARCHAR (100),
    hu_00               DECIMAL (10, 0),
    hu_00_unit          VARCHAR (5),
    hu_00_hour          INTEGER (10),
    hu_06               DECIMAL (10, 0),
    hu_06_unit          VARCHAR (5),
    hu_06_hour          INTEGER (10),
    hu_12_unit          VARCHAR (5),
    hu_12_hour          INTEGER (10),
    hu_12               DECIMAL (10, 6),
    hu_18_unit          VARCHAR (5),
    hu_18_hour          INTEGER (10),
    hu_18               DECIMAL (10, 6),
    hu_24_unit          VARCHAR (5),
    hu_24_hour          INTEGER (10),
    hu_24               DECIMAL (10, 6),
    hu_30_unit          VARCHAR (5),
    hu_30_hour          INTEGER (10),
    hu_30               DECIMAL (10, 6),
    hu_36_unit          VARCHAR (5),
    hu_36_hour          INTEGER (10),
    hu_36               DECIMAL (10, 6),
    hu_42_unit          VARCHAR (5),
    hu_42_hour          INTEGER (10),
    hu_42               DECIMAL (10, 6),
    hu_48_unit          VARCHAR (5),
    hu_48_hour          INTEGER (10),
    hu_48               DECIMAL (10, 6),
    hu_54_unit          VARCHAR (5),
    hu_54_hour          INTEGER (10),
    hu_54               DECIMAL (10, 6),
    hu_60_unit          VARCHAR (5),
    hu_60_hour          INTEGER (10),
    hu_60               DECIMAL (10, 6),
    hu_66_hour          INTEGER (10),
    hu_66_unit          VARCHAR (5),
    hu_66               DECIMAL (10, 6),
    hu_72_unit          VARCHAR (5),
    hu_72_hour          INTEGER (10),
    hu_72               DECIMAL (10, 6),
    hu_78_unit          VARCHAR (5),
    hu_78_hour          INTEGER (10),
    hu_78               DECIMAL (10, 6),
    humax_id            VARCHAR (50),
    humax_description   VARCHAR (100),
    humax_type          VARCHAR (100),
    humax_unit          VARCHAR (5),
    humax_1_day         DATETIME,
    humax_1             DECIMAL (10, 6),
    humax_2_day         DATETIME,
    humax_2             DECIMAL (10, 6),
    humax_3_day         DATETIME,
    humax_3             DECIMAL (10, 6),
    tmax_id             VARCHAR (50),
    tmax_description    VARCHAR (100),
    tmax_type           VARCHAR (100),
    tmax_c_unit         VARCHAR (5),
    tmax_f_unit         VARCHAR (5),
    tmax_1_day          DATETIME,
    tmax_1_c            DECIMAL (10, 6),
    tmax_1_f            DECIMAL (10, 6),
    tmax_2_day          DATETIME,
    tmax_2_c            DECIMAL (10, 6),
    tmax_2_f            DECIMAL (10, 6),
    tmax_3_day          DATETIME,
    tmax_3_c            DECIMAL (10, 0),
    tmax_3_f            DECIMAL (10, 0),
    humin_id            VARCHAR (5),
    humin_description   VARCHAR (100),
    humin_type          VARCHAR (10),
    humin_unit          VARCHAR (5),
    humin_1_day         DATETIME,
    humin_1             DECIMAL (10, 6),
    humin_2_day         DATETIME,
    humin_2             DECIMAL (10, 6),
    humin_3_day         DATETIME,
    humin_3             DECIMAL (10, 6),
    tmin_id             VARCHAR (50),
    tmin_description    VARCHAR (100),
    tmin_type           VARCHAR (100),
    tmin_c_unit         VARCHAR (20),
    tmin_f_unit         VARCHAR (20),
    tmin_1_day          DATETIME,
    tmin_1_c            DECIMAL (10, 6),
    tmin_1_f            DECIMAL (10, 6),
    tmin_2_day          DATETIME,
    tmin_2_c            DECIMAL (10, 6),
    tmin_2_f            DECIMAL (10, 6),
    tmin_3_day          DATETIME,
    tmin_3_c            DECIMAL (10, 6),
    tmin_3_f            DECIMAL (10, 6),
    t_id                VARCHAR (50),
    t_description       VARCHAR (100),
    t_type              VARCHAR (100),
    t_00_hour           INTEGER (5),
    t_00_c_unit         VARCHAR (5),
    t_00_f_unit         VARCHAR (5),
    t_00_c              DECIMAL (10, 6),
    t_00_f              DECIMAL (10, 6),
    t_06_hour           INTEGER (5),
    t_06_c_unit         VARCHAR (5),
    t_06_f_unit         VARCHAR (5),
    t_06_c              DECIMAL (10, 6),
    t_06_f              DECIMAL (10, 6),
    t_12_hour           INTEGER (5),
    t_12_c_unit         VARCHAR (5),
    t_12_f_unit         VARCHAR (5),
    t_12_c              DECIMAL (10, 6),
    t_12_f              DECIMAL (10, 6),
    t_18_hour           INTEGER (5),
    t_18_c_unit         VARCHAR (5),
    t_18_f_unit         VARCHAR (5),
    t_18_c              DECIMAL (10, 6),
    t_18_f              DECIMAL (10, 6),
    t_24_hour           INTEGER (5),
    t_24_c_unit         VARCHAR (5),
    t_24_f_unit         VARCHAR (5),
    t_24_c              DECIMAL (10, 6),
    t_24_f              DECIMAL (10, 6),
    t_30_hour           INTEGER (10),
    t_30_c_unit         VARCHAR (5),
    t_30_f_unit         VARCHAR (5),
    t_30_c              DECIMAL (10, 6),
    t_30_f              DECIMAL (10, 6),
    t_36_hour           INTEGER (10),
    t_36_c_unit         VARCHAR (5),
    t_36_f_unit         VARCHAR (5),
    t_36_c              DECIMAL (10, 6),
    t_36_f              DECIMAL (10, 6),
    t_42_hour           INTEGER (10),
    t_42_c_unit         VARCHAR (5),
    t_42_f_unit         VARCHAR (5),
    t_42_c              DECIMAL (10, 6),
    t_42_f              DECIMAL (10, 6),
    t_48_hour           INTEGER (10),
    t_48_c_unit         VARCHAR (5),
    t_48_f_unit         VARCHAR (5),
    t_48_c              DECIMAL (10, 6),
    t_48_f              DECIMAL (10, 6),
    t_54_hour           INTEGER (10),
    t_54_c_unit         VARCHAR (5),
    t_54_f_unit         VARCHAR (5),
    t_54_c              DECIMAL (10, 6),
    t_54_f              DECIMAL (10, 6),
    t_60_hour           INTEGER (10),
    t_60_c_unit         VARCHAR (5),
    t_60_f_unit         VARCHAR (5),
    t_60_c              DECIMAL (10, 6),
    t_60_f              DECIMAL (10, 6),
    t_66_hour           INTEGER (10),
    t_66_c_unit         VARCHAR (5),
    t_66_f_unit         VARCHAR (5),
    t_66_c              DECIMAL (10, 6),
    t_66_f              DECIMAL (10, 6),
    t_72_hour           INTEGER (10),
    t_72_c_unit         VARCHAR (5),
    t_72_f_unit         VARCHAR (5),
    t_72_c              DECIMAL (10, 6),
    t_72_f              DECIMAL (10, 6),
    t_78_hour           INTEGER (10),
    t_78_c_unit         VARCHAR (5),
    t_78_f_unit         VARCHAR (5),
    t_78_c              DECIMAL (10, 6),
    t_78_f              DECIMAL (10, 6),
    weather_id          VARCHAR (50),
    weather_description VARCHAR (100),
    weather_type        VARCHAR (100),
    weather_00          INTEGER (5),
    weather_00_unit     VARCHAR (5),
    weather_00_hour     INTEGER (10),
    weather_06          INTEGER (5),
    weather_06_unit     VARCHAR (5),
    weather_06_hour     INTEGER (10),
    weather_12          INTEGER (5),
    weather_12_unit     VARCHAR (5),
    weather_12_hour     INTEGER (10),
    weather_18          INTEGER (5),
    weather_18_unit     VARCHAR (5),
    weather_18_hour     INTEGER (10),
    weather_24          INTEGER (5),
    weather_24_unit     VARCHAR (5),
    weather_24_hour     INTEGER (10),
    weather_30_unit     VARCHAR (5),
    weather_30_hour     INTEGER (10),
    weather_30          INTEGER (5),
    weather_36_unit     VARCHAR (5),
    weather_36_hour     INTEGER (10),
    weather_36          INTEGER (5),
    weather_42_unit     VARCHAR (5),
    weather_42_hour     INTEGER (10),
    weather_42          INTEGER (5),
    weather_48_unit     VARCHAR (5),
    weather_48_hour     INTEGER (10),
    weather_48          INTEGER (5),
    weather_54          INTEGER (5),
    weather_54_unit     VARCHAR (5),
    weather_54_hour     INTEGER (10),
    weather_60          INTEGER (5),
    weather_60_unit     VARCHAR (5),
    weather_60_hour     INTEGER (10),
    weather_66          INTEGER (5),
    weather_72          INTEGER (5),
    weather_72_unit     VARCHAR (5),
    weather_72_hour     INTEGER (10),
    weather_78          INTEGER (5),
    weather_78_unit     VARCHAR (5),
    weather_78_hour     INTEGER (10),
    wd_id               VARCHAR (50),
    wd_description      VARCHAR (100),
    wd_type             VARCHAR (100),
    wd_00_deg_unit      VARCHAR (5),
    wd_00_card_unit     VARCHAR (5),
    wd_00_sexa_unit     VARCHAR (5),
    wd_00_deg           DECIMAL (10, 6),
    wd_00_card          VARCHAR (50),
    wd_00_sexa          INTEGER (10),
    wd_06_hour          INTEGER (5),
    wd_06_deg_unit      VARCHAR (5),
    wd_06_card_unit     VARCHAR (5),
    wd_06_sexa_unit     VARCHAR (5),
    wd_06_deg           DECIMAL (10, 6),
    wd_06_card          VARCHAR (50),
    wd_06_sexa          INTEGER (10),
    wd_12_hour          INTEGER (5),
    wd_12_deg_unit      VARCHAR (5),
    wd_12_card_unit     VARCHAR (5),
    wd_12_sexa_unit     VARCHAR (5),
    wd_12_deg           DECIMAL (10, 6),
    wd_12_card          VARCHAR (50),
    wd_12_sexa          INTEGER (10),
    wd_18_hour          INTEGER (5),
    wd_18_deg_unit      VARCHAR (5),
    wd_18_card_unit     VARCHAR (5),
    wd_18_sexa_unit     VARCHAR (5),
    wd_18_deg           DECIMAL (10, 6),
    wd_18_card          VARCHAR (50),
    wd_18_sexa          INTEGER (10),
    wd_24_hour          INTEGER (5),
    wd_24_deg_unit      VARCHAR (5),
    wd_24_card_unit     VARCHAR (5),
    wd_24_sexa_unit     VARCHAR (5),
    wd_24_deg           DECIMAL (10, 6),
    wd_24_card          VARCHAR (50),
    wd_24_sexa          INTEGER (10),
    wd_30_hour          INTEGER (5),
    wd_30_deg_unit      VARCHAR (5),
    wd_30_card_unit     VARCHAR (5),
    wd_30_sexa_unit     VARCHAR (5),
    wd_30_deg           DECIMAL (10, 6),
    wd_30_card          VARCHAR (50),
    wd_30_sexa          INTEGER (10),
    wd_36_hour          INTEGER (5),
    wd_36_deg_unit      VARCHAR (5),
    wd_36_card_unit     VARCHAR (5),
    wd_36_sexa_unit     VARCHAR (5),
    wd_36_deg           DECIMAL (10, 6),
    wd_36_card          VARCHAR (50),
    wd_36_sexa          INTEGER (10),
    wd_42_hour          INTEGER (5),
    wd_42_deg_unit      VARCHAR (5),
    wd_42_card_unit     VARCHAR (5),
    wd_42_sexa_unit     VARCHAR (5),
    wd_42_deg           DECIMAL (10, 6),
    wd_42_card          VARCHAR (50),
    wd_42_sexa          INTEGER (10),
    wd_48_hour          INTEGER (5),
    wd_48_deg_unit      VARCHAR (5),
    wd_48_card_unit     VARCHAR (5),
    wd_48_sexa_unit     VARCHAR (5),
    wd_48_deg           DECIMAL (10, 6),
    wd_48_card          VARCHAR (50),
    wd_48_sexa          INTEGER (10),
    wd_54_hour          INTEGER (5),
    wd_54_deg_unit      VARCHAR (5),
    wd_54_card_unit     VARCHAR (5),
    wd_54_sexa_unit     VARCHAR (5),
    wd_54_deg           DECIMAL (10, 6),
    wd_54_card          VARCHAR (50),
    wd_54_sexa          INTEGER (10),
    wd_60_hour          INTEGER (5),
    wd_60_deg_unit      VARCHAR (5),
    wd_60_card_unit     VARCHAR (5),
    wd_60_sexa_unit     VARCHAR (5),
    wd_60_deg           DECIMAL (10, 6),
    wd_60_card          VARCHAR (50),
    wd_60_sexa          INTEGER (10),
    wd_66_hour          INTEGER (5),
    wd_66_deg_unit      VARCHAR (5),
    wd_66_card_unit     VARCHAR (5),
    wd_66_sexa_unit     VARCHAR (5),
    wd_66_deg           DECIMAL (10, 6),
    wd_66_card          VARCHAR (50),
    wd_66_sexa          INTEGER (10),
    wd_72_hour          INTEGER (5),
    wd_72_deg_unit      VARCHAR (5),
    wd_72_card_unit     VARCHAR (5),
    wd_72_sexa_unit     VARCHAR (5),
    wd_72_deg           DECIMAL (10, 6),
    wd_72_card          VARCHAR (50),
    wd_72_sexa          INTEGER (10),
    wd_78_hour          INTEGER (5),
    wd_78_deg_unit      VARCHAR (5),
    wd_78_card_unit     VARCHAR (5),
    wd_78_sexa_unit     VARCHAR (5),
    wd_78_deg           DECIMAL (10, 6),
    wd_78_card          VARCHAR (50),
    wd_78_sexa          INTEGER (10),
    ws_id               VARCHAR (50),
    ws_description      VARCHAR (100),
    ws_type             VARCHAR (100),
    ws_00_hour          INTEGER (10),
    ws_00_mph_unit      VARCHAR (5),
    ws_00_kph_unit      VARCHAR (5),
    ws_00_ms_unit       VARCHAR (5),
    ws_00_kt_unit       VARCHAR (5),
    ws_00_mph           DECIMAL (10, 6),
    ws_00_kph           DECIMAL (10, 6),
    ws_00_ms            DECIMAL (10, 6),
    ws_00_kt            INTEGER (11),
    ws_06_hour          INTEGER (10),
    ws_06_mph_unit      VARCHAR (5),
    ws_06_kph_unit      VARCHAR (5),
    ws_06_ms_unit       VARCHAR (5),
    ws_06_kt_unit       VARCHAR (5),
    ws_06_mph           DECIMAL (10, 6),
    ws_06_kph           DECIMAL (10, 6),
    ws_06_ms            DECIMAL (10, 6),
    ws_06_kt            INTEGER (11),
    ws_12_hour          INTEGER (10),
    ws_12_mph_unit      VARCHAR (5),
    ws_12_kph_unit      VARCHAR (5),
    ws_12_ms_unit       VARCHAR (5),
    ws_12_kt_unit       VARCHAR (5),
    ws_12_mph           DECIMAL (10, 6),
    ws_12_kph           DECIMAL (10, 6),
    ws_12_ms            DECIMAL (10, 6),
    ws_12_kt            INTEGER (11),
    ws_18_hour          INTEGER (10),
    ws_18_mph_unit      VARCHAR (5),
    ws_18_kph_unit      VARCHAR (5),
    ws_18_ms_unit       VARCHAR (5),
    ws_18_kt_unit       VARCHAR (5),
    ws_18_mph           DECIMAL (10, 6),
    ws_18_kph           DECIMAL (10, 6),
    ws_18_ms            DECIMAL (10, 6),
    ws_18_kt            INTEGER (11),
    ws_24_hour          INTEGER (10),
    ws_24_mph_unit      VARCHAR (5),
    ws_24_kph_unit      VARCHAR (5),
    ws_24_ms_unit       VARCHAR (5),
    ws_24_kt_unit       VARCHAR (5),
    ws_24_mph           DECIMAL (10, 6),
    ws_24_kph           DECIMAL (10, 6),
    ws_24_ms            DECIMAL (10, 6),
    ws_24_kt            INTEGER (11),
    ws_30_hour          INTEGER (10),
    ws_30_mph_unit      VARCHAR (5),
    ws_30_kph_unit      VARCHAR (5),
    ws_30_ms_unit       VARCHAR (5),
    ws_30_kt_unit       VARCHAR (5),
    ws_30_mph           DECIMAL (10, 6),
    ws_30_kph           DECIMAL (10, 6),
    ws_30_ms            DECIMAL (10, 6),
    ws_30_kt            INTEGER (11),
    ws_36_hour          INTEGER (10),
    ws_36_mph_unit      VARCHAR (5),
    ws_36_kph_unit      VARCHAR (5),
    ws_36_ms_unit       VARCHAR (5),
    ws_36_kt_unit       VARCHAR (5),
    ws_36_mph           DECIMAL (10, 6),
    ws_36_kph           DECIMAL (10, 6),
    ws_36_ms            DECIMAL (10, 6),
    ws_36_kt            INTEGER (11),
    ws_42_hour          INTEGER (10),
    ws_42_mph_unit      VARCHAR (5),
    ws_42_kph_unit      VARCHAR (5),
    ws_42_ms_unit       VARCHAR (5),
    ws_42_kt_unit       VARCHAR (5),
    ws_42_mph           DECIMAL (10, 6),
    ws_42_kph           DECIMAL (10, 6),
    ws_42_ms            DECIMAL (10, 6),
    ws_42_kt            INTEGER (11),
    ws_48_hour          INTEGER (10),
    ws_48_mph_unit      VARCHAR (5),
    ws_48_kph_unit      VARCHAR (5),
    ws_48_ms_unit       VARCHAR (5),
    ws_48_kt_unit       VARCHAR (5),
    ws_48_mph           DECIMAL (10, 6),
    ws_48_kph           DECIMAL (10, 6),
    ws_48_ms            DECIMAL (10, 6),
    ws_48_kt            INTEGER (11),
    ws_54_hour          INTEGER (10),
    ws_54_mph_unit      VARCHAR (5),
    ws_54_kph_unit      VARCHAR (5),
    ws_54_ms_unit       VARCHAR (5),
    ws_54_kt_unit       VARCHAR (5),
    ws_54_mph           DECIMAL (10, 6),
    ws_54_kph           DECIMAL (10, 6),
    ws_54_ms            DECIMAL (10, 6),
    ws_54_kt            INTEGER (11),
    ws_60_hour          INTEGER (10),
    ws_60_mph_unit      VARCHAR (5),
    ws_60_kph_unit      VARCHAR (5),
    ws_60_ms_unit       VARCHAR (5),
    ws_60_kt_unit       VARCHAR (5),
    ws_60_mph           DECIMAL (10, 6),
    ws_60_kph           DECIMAL (10, 6),
    ws_60_ms            DECIMAL (10, 6),
    ws_60_kt            INTEGER (11),
    ws_66_hour          INTEGER (10),
    ws_66_mph_unit      VARCHAR (5),
    ws_66_kph_unit      VARCHAR (5),
    ws_66_ms_unit       VARCHAR (5),
    ws_66_kt_unit       VARCHAR (5),
    ws_66_mph           DECIMAL (10, 6),
    ws_66_kph           DECIMAL (10, 6),
    ws_66_ms            DECIMAL (10, 6),
    ws_66_kt            INTEGER (11),
    ws_72_hour          INTEGER (10),
    ws_72_mph_unit      VARCHAR (5),
    ws_72_kph_unit      VARCHAR (5),
    ws_72_ms_unit       VARCHAR (5),
    ws_72_kt_unit       VARCHAR (5),
    ws_72_mph           DECIMAL (10, 6),
    ws_72_kph           DECIMAL (10, 6),
    ws_72_ms            DECIMAL (10, 6),
    ws_72_kt            INTEGER (11),
    ws_78_hour          INTEGER (10),
    ws_78_mph_unit      VARCHAR (5),
    ws_78_kph_unit      VARCHAR (5),
    ws_78_ms_unit       VARCHAR (5),
    ws_78_kt_unit       VARCHAR (5),
    ws_78_mph           DECIMAL (10, 6),
    ws_78_kph           DECIMAL (10, 6),
    ws_78_ms            DECIMAL (10, 6),
    ws_78_kt            INTEGER (11)
);

-- Table: gempa_dirasakan
CREATE TABLE gempa_dirasakan (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), tanggal DATETIME , bujur DECIMAL (10, 6) , lintang DECIMAL (10, 6) , coordinate VARCHAR (200) , magnitude DECIMAL (10, 6) , magnitude_unit VARCHAR (20) , kedalaman DECIMAL (10, 6) , kedalaman_unit VARCHAR (20) , symbol VARCHAR (200) , keterangan VARCHAR (200), dirasakan VARCHAR (200));

-- Table: gempa_terkini
CREATE TABLE gempa_terkini (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), tanggal DATETIME , bujur DECIMAL (10, 6) , lintang DECIMAL (10, 6) , coordinate VARCHAR (200) , magnitude DECIMAL (10, 6) , magnitude_unit VARCHAR (20) , kedalaman DECIMAL (10, 6) , kedalaman_unit VARCHAR (20) , symbol VARCHAR (200) , wilayah VARCHAR (200));

-- Table: gempa_terkini_csv
CREATE TABLE gempa_terkini_csv (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), src VARCHAR (200) , eqid VARCHAR (200) , datetime DATETIME , longitude DECIMAL (10, 6) , latitude DECIMAL (10, 6) , coordinate VARCHAR (200) , magnitude DECIMAL (10, 6) , depth DECIMAL (10, 6) , region VARCHAR (200));

-- Table: maritim_cuaca_pelabuhan
CREATE TABLE maritim_cuaca_pelabuhan (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), domain VARCHAR (50) , station_id INTEGER (5) , shortname VARCHAR (100) , timestamp DATETIME , phone_number VARCHAR (50) , phone_id VARCHAR (50) , email VARCHAR (100) , address VARCHAR (100) , port_id INTEGER (10) , port_name VARCHAR (100) , port_description VARCHAR (100) , port_domain VARCHAR (50) , port_longitude DECIMAL (10, 6) , port_latitude DECIMAL (10, 6) , port_coordinate VARCHAR (200) , type VARCHAR (50), datetime DATETIME, validfrom DATETIME, validto DATETIME, timezone VARCHAR (50), weather_id VARCHAR (50), weather_description VARCHAR (100), weather_icon_unit VARCHAR (20), weather_icon VARCHAR (50), wd_from_id VARCHAR (50), wd_from_description VARCHAR (100), wd_from_icon_id_unit VARCHAR (20), wd_from_icon_en_unit VARCHAR (20), wd_from_icon_card_unit VARCHAR (20), wd_from_icon_id VARCHAR (50), wd_from_icon_en VARCHAR (50), wd_from_icon_card VARCHAR (50), wd_to_id VARCHAR (50), wd_to_description VARCHAR (100), wd_to_icon_en_unit VARCHAR (20), wd_to_icon_id_unit VARCHAR (20), wd_to_icon_card_unit VARCHAR (20), wd_to_icon_en VARCHAR (50), wd_to_icon_id VARCHAR (50), wd_to_icon_card VARCHAR (50), ws_min_id VARCHAR (50), ws_min_description VARCHAR (100), ws_min_unit VARCHAR (20), ws_min INTEGER (10), ws_max_id VARCHAR (50), ws_max_description VARCHAR (100), ws_max_unit VARCHAR (20), ws_max INTEGER (10), wave_min_id VARCHAR (50), wave_min_description VARCHAR (100), wave_min_unit VARCHAR (20), wave_min DECIMAL (10, 6), wave_max_id VARCHAR (50), wave_max_description VARCHAR (100), wave_max_unit VARCHAR (20), wave_max DECIMAL (10, 6), visibility_id VARCHAR (50), visibility_description VARCHAR (100), visibility_unit VARCHAR (50), visibility DECIMAL (20, 6), tmin_id VARCHAR (50), tmin_description VARCHAR (100), tmin_unit VARCHAR (20), tmin DECIMAL (10, 6), tmax_id VARCHAR (50), tmax_description VARCHAR (100), tmax_unit VARCHAR (20), tmax DECIMAL (10, 6), humin_id VARCHAR (50), humin_description VARCHAR (100), humin_unit VARCHAR (20), humin DECIMAL (10, 6), humax_id VARCHAR (50), humax_description VARCHAR (100), humax_unit VARCHAR (20), humax DECIMAL (10, 6), pdf_id VARCHAR (50), pdf_description VARCHAR (50), pdf_unit VARCHAR (50), pdf VARCHAR (200), pasang_min_datemin DATETIME, pasang_min_datemax DATETIME, pasang_min_unit VARCHAR (50), pasang_min_description VARCHAR (100), pasang_min_zona VARCHAR (50), pasang_min DECIMAL (10, 6), pasang_max_datemin DATETIME, pasang_max_datemax DATETIME, pasang_max_unit VARCHAR (50), pasang_max_description VARCHAR (100), pasang_max_zona VARCHAR (50), pasang_max DECIMAL (10, 6), remarks VARCHAR (400));

-- Table: maritim_cuaca_pelayanan
CREATE TABLE maritim_cuaca_pelayanan (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), domain VARCHAR (50) , station_id INTEGER (5) , shortname VARCHAR (100) , timestamp DATETIME , phone_number VARCHAR (50) , phone_id VARCHAR (50) , email VARCHAR (100) , address VARCHAR (100) , file_pdf VARCHAR (200), type VARCHAR (50), datetime DATETIME, validfrom DATETIME, validto DATETIME, timezone VARCHAR (50), area_id VARCHAR (50), area_name VARCHAR (100), area_description VARCHAR (100), area_domain VARCHAR (50), weather_id VARCHAR (50), weather_description VARCHAR (100), weather_icon_id_unit VARCHAR (20), weather_icon_en_unit VARCHAR (20), weather_icon_id VARCHAR (50), weather_icon_en VARCHAR (50), wd_from_id VARCHAR (50), wd_from_description VARCHAR (100), wd_from_icon_id_unit VARCHAR (20), wd_from_icon_en_unit VARCHAR (20), wd_from_card_unit VARCHAR (20), wd_from_icon_id VARCHAR (50), wd_from_icon_en VARCHAR (50), wd_from_card VARCHAR (50), wd_to_id VARCHAR (50), wd_to_description VARCHAR (100), wd_to_icon_id_unit VARCHAR (20), wd_to_icon_en_unit VARCHAR (20), wd_to_card_unit VARCHAR (20), wd_to_icon_id VARCHAR (50), wd_to_icon_en VARCHAR (50), wd_to_card VARCHAR (50), ws_min_id VARCHAR (50), ws_min_description VARCHAR (100), ws_min_unit VARCHAR (20), ws_min INTEGER (10), ws_max_id VARCHAR (50), ws_max_description VARCHAR (100), ws_max_unit VARCHAR (20), ws_max INTEGER (10), wave_min_id VARCHAR (50), wave_min_description VARCHAR (100), wave_min_unit VARCHAR (20), wave_min DECIMAL (10, 6), wave_max_id VARCHAR (50), wave_max_description VARCHAR (100), wave_max_unit VARCHAR (20), wave_max DECIMAL (10, 6), status_warning_id VARCHAR (50), status_warning_description VARCHAR (100), status_warning_unit VARCHAR (20), status_warning VARCHAR (200), hari VARCHAR (50), peringatan_dini TEXT, kondisi_synoptik TEXT);

-- Table: maritim_cuaca_penyebrangan
CREATE TABLE maritim_cuaca_penyebrangan (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), domain VARCHAR (50) , id_xml VARCHAR (50) , id_area VARCHAR (50) , id_asdp VARCHAR (50) , station_id INTEGER (5) , arah_angin_dari INTEGER (5) , arah_angin_sampai INTEGER (5) ,  shortname VARCHAR (100) , timestamp DATETIME , created_date DATETIME , modified_date DATETIME , created_by INTEGER (10) ,  modified_by INTEGER (10) , phone_number VARCHAR (50) , phone_id VARCHAR (50) , email VARCHAR (100) , address VARCHAR (100) , area_id INTEGER (10) , area_name_id VARCHAR (100) , area_name_en VARCHAR (100) , area_description VARCHAR (100) , area_domain VARCHAR (50) , area_habor_from VARCHAR (50), area_habor_to VARCHAR (50) , type VARCHAR (50), datetime DATETIME, validfrom DATETIME, validto DATETIME, timezone VARCHAR (50), weather_id VARCHAR (50), weather_description VARCHAR (100), weather_icon_unit VARCHAR (20), weather_icon VARCHAR (50), wd_from_id VARCHAR (50), wd_from_description VARCHAR (100), wd_from_icon_id_unit VARCHAR (20), wd_from_icon_en_unit VARCHAR (20), wd_from_icon_card_unit VARCHAR (20), wd_from_icon_id VARCHAR (50), wd_from_icon_en VARCHAR (50), wd_from_icon_card VARCHAR (50), wd_to_id VARCHAR (50), wd_to_description VARCHAR (100), wd_to_icon_en_unit VARCHAR (20), wd_to_icon_id_unit VARCHAR (20), wd_to_icon_card_unit VARCHAR (20), wd_to_icon_en VARCHAR (50), wd_to_icon_id VARCHAR (50), wd_to_icon_card VARCHAR (50), ws_min_id VARCHAR (50), ws_min_description VARCHAR (100), ws_min_unit VARCHAR (20), ws_min INTEGER (10), ws_max_id VARCHAR (50), ws_max_description VARCHAR (100), ws_max_unit VARCHAR (20), ws_max INTEGER (10), wave_min_id VARCHAR (50), wave_min_description VARCHAR (100), wave_min_unit VARCHAR (20), wave_min DECIMAL (10, 6), wave_max_id VARCHAR (50), wave_max_description VARCHAR (100), wave_max_unit VARCHAR (20), wave_max DECIMAL (10, 6), pdf_id VARCHAR (50), pdf_description VARCHAR (50), pdf_unit VARCHAR (50), pdf VARCHAR (200));

-- Table: maritim_wisata_bahari
CREATE TABLE maritim_wisata_bahari (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), domain VARCHAR (50) , station_id INTEGER (5) , shortname VARCHAR (100) , timestamp DATETIME , phone_number VARCHAR (50) , phone_id VARCHAR (50) , email VARCHAR (100) , address VARCHAR (100) , beach_id INTEGER (10) , beach_name VARCHAR (100) , beach_description VARCHAR (100) , beach_domain VARCHAR (50) , beach_longitude DECIMAL (10, 6) , beach_latitude DECIMAL (10, 6) , beach_coordinate VARCHAR (200) , type VARCHAR (50), datetime DATETIME, hour INTEGER (10), wave_id VARCHAR (50), wave_description VARCHAR (100), wave_direction_unit VARCHAR (20), wave_deg_unit VARCHAR (20), wave_direction VARCHAR (50), wave_deg DECIMAL (10, 6), wave_height_id VARCHAR (50), wave_height_description VARCHAR (100), wave_height_meter_unit VARCHAR (20), wave_height_feet_unit VARCHAR (20), wave_height_meter DECIMAL (10, 6), wave_height_feet DECIMAL (10, 6), weather_id VARCHAR (50), weather_description VARCHAR (100), weather_unit VARCHAR (20), weather INTEGER (10), wd_id VARCHAR (50), wd_description VARCHAR (100), wd_deg_unit VARCHAR (20), wd_card_unit VARCHAR (20), wd_sexa_unit VARCHAR (20), wd_deg DECIMAL (10, 6), wd_card VARCHAR (50), wd_sexa INTEGER (20), ws_id VARCHAR (50), ws_description VARCHAR (100), ws_kt_unit VARCHAR (20), ws_mph_unit VARCHAR (20), ws_kt INTEGER (10), ws_mph DECIMAL (10, 6));

-- Table: satelit_himawari_8_ir_enhanced
CREATE TABLE satelit_himawari_8_ir_enhanced (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), judul VARCHAR (100)  DEFAULT ('0'), narasi VARCHAR (512)  DEFAULT ('0'), lokasi VARCHAR (100)  DEFAULT ('0'), file VARCHAR (100)  DEFAULT ('0'));

-- Table: satelit_himawari_8_natural_color
CREATE TABLE satelit_himawari_8_natural_color (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), judul VARCHAR (100)  DEFAULT ('0'), narasi VARCHAR (512)  DEFAULT ('0'), lokasi VARCHAR (100)  DEFAULT ('0'), file VARCHAR (100)  DEFAULT ('0'));

-- Table: satelit_hotspot_modis
CREATE TABLE satelit_hotspot_modis (pk INTEGER PRIMARY KEY AUTOINCREMENT , batch_time TIMESTAMP  DEFAULT (CURRENT_TIMESTAMP), judul VARCHAR (100)  DEFAULT ('0'), narasi VARCHAR (512)  DEFAULT ('0'), lokasi VARCHAR (100)  DEFAULT ('0'), file VARCHAR (100)  DEFAULT ('0'));

-- Table: iklim_kabupaten_csv
CREATE TABLE iklim_kabupaten_csv (
    pk                  INTEGER         PRIMARY KEY AUTOINCREMENT
                                        ,
    batch_time          TIMESTAMP       
                                        DEFAULT (CURRENT_TIMESTAMP),
    provinsi            VARCHAR (30),
    id_kabupaten_kota   INTEGER (5),
    kabupaten_kota      VARCHAR (30),
    month               INTEGER (5),
    year                INTEGER (5),
    ach_1_sbk           TEXT,
    ach_1_sb            TEXT,
    ach_1_sbb           TEXT,
    ach_1_m             TEXT,
    ash_1_sbk           TEXT,
    ash_1_sb            TEXT,
    ash_1_sbb           TEXT,
    ash_1_m             TEXT,
    pch_1_sbk           TEXT,
    pch_1_sb            TEXT,
    pch_1_sbb           TEXT,
    pch_1_m             TEXT,
    psh_1_sbk           TEXT,
    psh_1_sb            TEXT,
    psh_1_sbb           TEXT,
    psh_1_m             TEXT,
    pch_2_sbk           TEXT,
    pch_2_sb            TEXT,
    pch_2_sbb           TEXT,
    pch_2_m             TEXT,
    psh_2_sbk           TEXT,
    psh_2_sb            TEXT,
    psh_2_sbb           TEXT,
    psh_2_m             TEXT,
    pch_3_sbk           TEXT,
    pch_3_sb            TEXT,
    pch_3_sbb           TEXT,
    pch_3_m             TEXT,
    psh_3_sbk           TEXT,
    psh_3_sb            TEXT,
    psh_3_sbb           TEXT,
    psh_3_m             TEXT
);

-- Table: iklim_kecamatan_csv
CREATE TABLE iklim_kecamatan_csv (
    pk                  INTEGER         PRIMARY KEY AUTOINCREMENT
                                        ,
    batch_time          TIMESTAMP       
                                        DEFAULT (CURRENT_TIMESTAMP),
    provinsi            VARCHAR (30),
    id_kabupaten_kota   INTEGER (5),
    kabupaten_kota      VARCHAR (30),
    id_kecamatan        INTEGER (8),
    kecamatan           VARCHAR (30),
    month               INTEGER (5),
    year                INTEGER (5),
    ach_1_sbk           TEXT,
    ach_1_sb            TEXT,
    ach_1_sbb           TEXT,
    ach_1_m             TEXT,
    ash_1_sbk           TEXT,
    ash_1_sb            TEXT,
    ash_1_sbb           TEXT,
    ash_1_m             TEXT,
    pch_1_sbk           TEXT,
    pch_1_sb            TEXT,
    pch_1_sbb           TEXT,
    pch_1_m             TEXT,
    psh_1_sbk           TEXT,
    psh_1_sb            TEXT,
    psh_1_sbb           TEXT,
    psh_1_m             TEXT,
    pch_2_sbk           TEXT,
    pch_2_sb            TEXT,
    pch_2_sbb           TEXT,
    pch_2_m             TEXT,
    psh_2_sbk           TEXT,
    psh_2_sb            TEXT,
    psh_2_sbb           TEXT,
    psh_2_m             TEXT,
    pch_3_sbk           TEXT,
    pch_3_sb            TEXT,
    pch_3_sbb           TEXT,
    pch_3_m             TEXT,
    psh_3_sbk           TEXT,
    psh_3_sb            TEXT,
    psh_3_sbb           TEXT,
    psh_3_m             TEXT
);

-- Table: iklim_desa_csv
CREATE TABLE iklim_desa_csv (
    pk                  INTEGER         PRIMARY KEY AUTOINCREMENT
                                        ,
    batch_time          TIMESTAMP       
                                        DEFAULT (CURRENT_TIMESTAMP),
    provinsi            VARCHAR (30),
    id_kabupaten_kota   INTEGER (5),
    kabupaten_kota      VARCHAR (30),
    id_kecamatan        INTEGER (8),
    kecamatan           VARCHAR (30),
    id_desa             INTEGER (12),
    desa                VARCHAR (30),
    month               INTEGER (5),
    year                INTEGER (5),
    ach_1_sbk           TEXT,
    ach_1_sb            TEXT,
    ach_1_sbb           TEXT,
    ach_1_m             TEXT,
    ash_1_sbk           TEXT,
    ash_1_sb            TEXT,
    ash_1_sbb           TEXT,
    ash_1_m             TEXT,
    pch_1_sbk           TEXT,
    pch_1_sb            TEXT,
    pch_1_sbb           TEXT,
    pch_1_m             TEXT,
    psh_1_sbk           TEXT,
    psh_1_sb            TEXT,
    psh_1_sbb           TEXT,
    psh_1_m             TEXT,
    pch_2_sbk           TEXT,
    pch_2_sb            TEXT,
    pch_2_sbb           TEXT,
    pch_2_m             TEXT,
    psh_2_sbk           TEXT,
    psh_2_sb            TEXT,
    psh_2_sbb           TEXT,
    psh_2_m             TEXT,
    pch_3_sbk           TEXT,
    pch_3_sb            TEXT,
    pch_3_sbb           TEXT,
    pch_3_m             TEXT,
    psh_3_sbk           TEXT,
    psh_3_sb            TEXT,
    psh_3_sbb           TEXT,
    psh_3_m             TEXT
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
