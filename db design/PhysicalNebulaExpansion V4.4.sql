/*
 Navicat Premium Data Transfer

 Source Server         : Postgres
 Source Server Type    : PostgreSQL
 Source Server Version : 130000
 Source Host           : localhost:5432
 Source Catalog        : testing6
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 130000
 File Encoding         : 65001

 Date: 14/01/2021 16:11:50
*/


-- ----------------------------
-- Sequence structure for Delivery_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."Delivery_id_seq";
CREATE SEQUENCE "public"."Delivery_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for Delivery_voucher_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."Delivery_voucher_seq";
CREATE SEQUENCE "public"."Delivery_voucher_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for Devolution_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."Devolution_id_seq";
CREATE SEQUENCE "public"."Devolution_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for Devolution_voucher_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."Devolution_voucher_seq";
CREATE SEQUENCE "public"."Devolution_voucher_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for Reception_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."Reception_id_seq";
CREATE SEQUENCE "public"."Reception_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for Reception_voucher_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."Reception_voucher_seq";
CREATE SEQUENCE "public"."Reception_voucher_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;

-- ----------------------------
-- Table structure for Cost Center
-- ----------------------------
DROP TABLE IF EXISTS "public"."Cost Center";
CREATE TABLE "public"."Cost Center" (
  "code" int2 NOT NULL,
  "name" char(50) COLLATE "pg_catalog"."default",
  "code_unit" char(15) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of Cost Center
-- ----------------------------

-- ----------------------------
-- Table structure for Cost_Center_Inventory
-- ----------------------------
DROP TABLE IF EXISTS "public"."Cost_Center_Inventory";
CREATE TABLE "public"."Cost_Center_Inventory" (
  "code_cost_center" int2 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4
)
;

-- ----------------------------
-- Records of Cost_Center_Inventory
-- ----------------------------

-- ----------------------------
-- Table structure for Delivery
-- ----------------------------
DROP TABLE IF EXISTS "public"."Delivery";
CREATE TABLE "public"."Delivery" (
  "id" int4 NOT NULL DEFAULT nextval('"Delivery_id_seq"'::regclass),
  "voucher" int4 NOT NULL DEFAULT nextval('"Delivery_voucher_seq"'::regclass),
  "date_stamp" date NOT NULL,
  "code_cost_center" int2 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_dispatcher" int8
)
;

-- ----------------------------
-- Records of Delivery
-- ----------------------------

-- ----------------------------
-- Table structure for Delivery_Inventory
-- ----------------------------
DROP TABLE IF EXISTS "public"."Delivery_Inventory";
CREATE TABLE "public"."Delivery_Inventory" (
  "id_delivery" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL
)
;

-- ----------------------------
-- Records of Delivery_Inventory
-- ----------------------------

-- ----------------------------
-- Table structure for Devolution
-- ----------------------------
DROP TABLE IF EXISTS "public"."Devolution";
CREATE TABLE "public"."Devolution" (
  "id" int4 NOT NULL DEFAULT nextval('"Devolution_id_seq"'::regclass),
  "code_provider" int4 NOT NULL,
  "voucher" int4 NOT NULL DEFAULT nextval('"Devolution_voucher_seq"'::regclass),
  "date_stamp" date NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_dispatcher" int8
)
;

-- ----------------------------
-- Records of Devolution
-- ----------------------------

-- ----------------------------
-- Table structure for Devolution_Inventory
-- ----------------------------
DROP TABLE IF EXISTS "public"."Devolution_Inventory";
CREATE TABLE "public"."Devolution_Inventory" (
  "id_devolution" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL
)
;

-- ----------------------------
-- Records of Devolution_Inventory
-- ----------------------------

-- ----------------------------
-- Table structure for Dispatcher
-- ----------------------------
DROP TABLE IF EXISTS "public"."Dispatcher";
CREATE TABLE "public"."Dispatcher" (
  "ci_person" int8 NOT NULL
)
;

-- ----------------------------
-- Records of Dispatcher
-- ----------------------------

-- ----------------------------
-- Table structure for Person
-- ----------------------------
DROP TABLE IF EXISTS "public"."Person";
CREATE TABLE "public"."Person" (
  "ci" int8 NOT NULL,
  "name" char(50) COLLATE "pg_catalog"."default",
  "last_name1" char(50) COLLATE "pg_catalog"."default",
  "last_name2" char(50) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of Person
-- ----------------------------

-- ----------------------------
-- Table structure for Product
-- ----------------------------
DROP TABLE IF EXISTS "public"."Product";
CREATE TABLE "public"."Product" (
  "code" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "account_sub1" int2,
  "account_sub2" int2,
  "description" char(50) COLLATE "pg_catalog"."default",
  "unit" char(10) COLLATE "pg_catalog"."default",
  "price" numeric(10,2) NOT NULL
)
;

-- ----------------------------
-- Records of Product
-- ----------------------------

-- ----------------------------
-- Table structure for Provider
-- ----------------------------
DROP TABLE IF EXISTS "public"."Provider";
CREATE TABLE "public"."Provider" (
  "code" int4 NOT NULL,
  "name" char(50) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of Provider
-- ----------------------------

-- ----------------------------
-- Table structure for Receiver
-- ----------------------------
DROP TABLE IF EXISTS "public"."Receiver";
CREATE TABLE "public"."Receiver" (
  "ci_person" int8 NOT NULL
)
;

-- ----------------------------
-- Records of Receiver
-- ----------------------------

-- ----------------------------
-- Table structure for Reception
-- ----------------------------
DROP TABLE IF EXISTS "public"."Reception";
CREATE TABLE "public"."Reception" (
  "id" int4 NOT NULL DEFAULT nextval('"Reception_id_seq"'::regclass),
  "code_provider" int4 NOT NULL,
  "voucher" int4 NOT NULL DEFAULT nextval('"Reception_voucher_seq"'::regclass),
  "bill_number" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "date_stamp" date NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_store_manager" int8
)
;

-- ----------------------------
-- Records of Reception
-- ----------------------------

-- ----------------------------
-- Table structure for Reception_Inventory
-- ----------------------------
DROP TABLE IF EXISTS "public"."Reception_Inventory";
CREATE TABLE "public"."Reception_Inventory" (
  "id_reception" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL
)
;

-- ----------------------------
-- Records of Reception_Inventory
-- ----------------------------

-- ----------------------------
-- Table structure for Store Manager
-- ----------------------------
DROP TABLE IF EXISTS "public"."Store Manager";
CREATE TABLE "public"."Store Manager" (
  "ci_person" int8 NOT NULL
)
;

-- ----------------------------
-- Records of Store Manager
-- ----------------------------

-- ----------------------------
-- Table structure for Unit
-- ----------------------------
DROP TABLE IF EXISTS "public"."Unit";
CREATE TABLE "public"."Unit" (
  "code" char(15) COLLATE "pg_catalog"."default" NOT NULL,
  "name" char(50) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of Unit
-- ----------------------------

-- ----------------------------
-- Table structure for Warehouse
-- ----------------------------
DROP TABLE IF EXISTS "public"."Warehouse";
CREATE TABLE "public"."Warehouse" (
  "number" int2 NOT NULL,
  "name" char(50) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of Warehouse
-- ----------------------------

-- ----------------------------
-- Table structure for Warehouse_Inventory
-- ----------------------------
DROP TABLE IF EXISTS "public"."Warehouse_Inventory";
CREATE TABLE "public"."Warehouse_Inventory" (
  "number_warehouse" int2 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL
)
;

-- ----------------------------
-- Records of Warehouse_Inventory
-- ----------------------------

-- ----------------------------
-- Function structure for fn_add_product_from_provider_to_warehouse
-- ----------------------------
DROP FUNCTION IF EXISTS "public"."fn_add_product_from_provider_to_warehouse"();
CREATE OR REPLACE FUNCTION "public"."fn_add_product_from_provider_to_warehouse"()
  RETURNS "pg_catalog"."trigger" AS $BODY$	
	DECLARE
	warehouse_id INTEGER;
	tmp_quantity FLOAT;	
	BEGIN
		
		warehouse_id := (SELECT "Reception".number_warehouse
								      FROM "Reception"
											  WHERE "Reception"."id" = NEW.id_reception AND
												      "Reception".code_provider = NEW.code_provider);
													
		tmp_quantity := (SELECT quantity
										  FROM "Warehouse_Inventory" 
											  WHERE  number_warehouse = warehouse_id AND
						                   code_product = NEW.code_product AND
									             code_provider = NEW.code_provider);
	  
		IF tmp_quantity IS NOT NULL THEN
			UPDATE "Warehouse_Inventory"
			  SET quantity = tmp_quantity + NEW.quantity
		    WHERE number_warehouse = warehouse_id AND
						  code_product = NEW.code_product AND
							code_provider = NEW.code_provider;
		ELSE		
		  INSERT INTO "Warehouse_Inventory"(number_warehouse,code_product,code_provider,quantity) 
		    VALUES(warehouse_id,NEW.code_product,NEW.code_provider,NEW.quantity);
	  END IF;

	RETURN NEW;
END$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;

-- ----------------------------
-- Function structure for fn_add_product_from_warehouse_to_cost_center
-- ----------------------------
DROP FUNCTION IF EXISTS "public"."fn_add_product_from_warehouse_to_cost_center"();
CREATE OR REPLACE FUNCTION "public"."fn_add_product_from_warehouse_to_cost_center"()
  RETURNS "pg_catalog"."trigger" AS $BODY$	
	DECLARE
	warehouse_id INTEGER;
	cost_center_id INTEGER;
	tmp_quantity FLOAT;	
	avaliable_quantity FLOAT;
	BEGIN
	
		warehouse_id := (SELECT number_warehouse
		                   FROM "Delivery"
											   WHERE "Delivery"."id" = NEW.id_delivery);
		
		cost_center_id := (SELECT "Delivery".code_cost_center
								         FROM "Delivery"
											     WHERE "Delivery"."id" = NEW.id_delivery);
													
		tmp_quantity := (SELECT quantity
										  FROM "Cost_Center_Inventory" 
											  WHERE code_product = NEW.code_product AND
									            code_provider = NEW.code_provider AND
															code_cost_center = cost_center_id);

		avaliable_quantity := (SELECT quantity
		                         FROM "Warehouse_Inventory"
														   WHERE code_product = NEW.code_product AND
		                                 code_provider = NEW.code_provider AND
																		 number_warehouse = warehouse_id);						
	  
		IF avaliable_quantity IS NULL OR avaliable_quantity < NEW.quantity THEN
		  RAISE EXCEPTION 'Not enough product';
    ELSE		
				UPDATE "Warehouse_Inventory"
				  SET quantity = quantity - NEW.quantity
					WHERE code_product = NEW.code_product AND
					      code_provider = NEW.code_provider AND
								number_warehouse = warehouse_id;
		
				IF tmp_quantity IS NOT NULL THEN
					UPDATE "Cost_Center_Inventory"
						SET quantity = tmp_quantity + NEW.quantity
						WHERE code_product = NEW.code_product AND
									code_provider = NEW.code_provider AND
									code_cost_center = cost_center_id;
				ELSE		
					INSERT INTO "Cost_Center_Inventory"(code_cost_center,code_product,code_provider,quantity) 
						VALUES(warehouse_id,NEW.code_product,NEW.code_provider,NEW.quantity);
				END IF;
		END IF;

	RETURN NEW;
END$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;

-- ----------------------------
-- Function structure for fn_return_product_from_warehouse_to_provider
-- ----------------------------
DROP FUNCTION IF EXISTS "public"."fn_return_product_from_warehouse_to_provider"();
CREATE OR REPLACE FUNCTION "public"."fn_return_product_from_warehouse_to_provider"()
  RETURNS "pg_catalog"."trigger" AS $BODY$	
	DECLARE
	warehouse_id INTEGER;
	avaliable_quantity FLOAT;
	BEGIN
	
		warehouse_id := (SELECT number_warehouse
		                   FROM "Devolution"
											   WHERE "Devolution"."id" = NEW.id_devolution AND
												       "Devolution".code_provider = NEW.code_provider);													
		
		avaliable_quantity := (SELECT quantity
		                         FROM "Warehouse_Inventory"
														   WHERE code_product = NEW.code_product AND
		                                 code_provider = NEW.code_provider AND
																		 number_warehouse = warehouse_id);						
	  
		IF avaliable_quantity IS NULL OR avaliable_quantity < NEW.quantity THEN
		  RAISE EXCEPTION 'Not enough product';
    ELSE		
				UPDATE "Warehouse_Inventory"
				  SET quantity = quantity - NEW.quantity
					WHERE code_product = NEW.code_product AND
					      code_provider = NEW.code_provider AND
								number_warehouse = warehouse_id;
		END IF;

	RETURN NEW;
END$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."Delivery_id_seq"
OWNED BY "public"."Delivery"."id";
SELECT setval('"public"."Delivery_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."Delivery_voucher_seq"
OWNED BY "public"."Delivery"."voucher";
SELECT setval('"public"."Delivery_voucher_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."Devolution_id_seq"
OWNED BY "public"."Devolution"."id";
SELECT setval('"public"."Devolution_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."Devolution_voucher_seq"
OWNED BY "public"."Devolution"."voucher";
SELECT setval('"public"."Devolution_voucher_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."Reception_id_seq"
OWNED BY "public"."Reception"."id";
SELECT setval('"public"."Reception_id_seq"', 2, false);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."Reception_voucher_seq"
OWNED BY "public"."Reception"."voucher";
SELECT setval('"public"."Reception_voucher_seq"', 2, false);

-- ----------------------------
-- Primary Key structure for table Cost Center
-- ----------------------------
ALTER TABLE "public"."Cost Center" ADD CONSTRAINT "_copy_16" PRIMARY KEY ("code");

-- ----------------------------
-- Primary Key structure for table Cost_Center_Inventory
-- ----------------------------
ALTER TABLE "public"."Cost_Center_Inventory" ADD CONSTRAINT "Cost_Center_Inventory_pkey" PRIMARY KEY ("code_cost_center", "code_product", "code_provider");

-- ----------------------------
-- Uniques structure for table Delivery
-- ----------------------------
ALTER TABLE "public"."Delivery" ADD CONSTRAINT "u_voucher_copy_2" UNIQUE ("voucher");

-- ----------------------------
-- Checks structure for table Delivery
-- ----------------------------
ALTER TABLE "public"."Delivery" ADD CONSTRAINT "different_responsable2" CHECK (ci_receiver <> ci_dispatcher);

-- ----------------------------
-- Primary Key structure for table Delivery
-- ----------------------------
ALTER TABLE "public"."Delivery" ADD CONSTRAINT "_copy_5" PRIMARY KEY ("id");

-- ----------------------------
-- Triggers structure for table Delivery_Inventory
-- ----------------------------
CREATE TRIGGER "tr_add_product_from_warehouse_to_cost_center" AFTER INSERT ON "public"."Delivery_Inventory"
FOR EACH ROW
EXECUTE PROCEDURE "public"."fn_add_product_from_warehouse_to_cost_center"();

-- ----------------------------
-- Primary Key structure for table Delivery_Inventory
-- ----------------------------
ALTER TABLE "public"."Delivery_Inventory" ADD CONSTRAINT "Delivery_Inventory_pkey" PRIMARY KEY ("id_delivery", "code_product", "code_provider");

-- ----------------------------
-- Uniques structure for table Devolution
-- ----------------------------
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "u_voucher_copy_1" UNIQUE ("voucher");
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "u_id_devolution" UNIQUE ("id");

-- ----------------------------
-- Checks structure for table Devolution
-- ----------------------------
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "different_responsable1" CHECK (ci_receiver <> ci_dispatcher);

-- ----------------------------
-- Primary Key structure for table Devolution
-- ----------------------------
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "_copy_4" PRIMARY KEY ("id", "code_provider");

-- ----------------------------
-- Triggers structure for table Devolution_Inventory
-- ----------------------------
CREATE TRIGGER "tr_return_product_from_warehouse_to_provider" AFTER INSERT ON "public"."Devolution_Inventory"
FOR EACH ROW
EXECUTE PROCEDURE "public"."fn_return_product_from_warehouse_to_provider"();

-- ----------------------------
-- Primary Key structure for table Devolution_Inventory
-- ----------------------------
ALTER TABLE "public"."Devolution_Inventory" ADD CONSTRAINT "Devolution_Inventory_pkey" PRIMARY KEY ("id_devolution", "code_product", "code_provider");

-- ----------------------------
-- Primary Key structure for table Dispatcher
-- ----------------------------
ALTER TABLE "public"."Dispatcher" ADD CONSTRAINT "_copy_10" PRIMARY KEY ("ci_person");

-- ----------------------------
-- Primary Key structure for table Person
-- ----------------------------
ALTER TABLE "public"."Person" ADD CONSTRAINT "_copy_13" PRIMARY KEY ("ci");

-- ----------------------------
-- Primary Key structure for table Product
-- ----------------------------
ALTER TABLE "public"."Product" ADD CONSTRAINT "_copy_2" PRIMARY KEY ("code", "code_provider");

-- ----------------------------
-- Primary Key structure for table Provider
-- ----------------------------
ALTER TABLE "public"."Provider" ADD CONSTRAINT "_copy_11" PRIMARY KEY ("code");

-- ----------------------------
-- Primary Key structure for table Receiver
-- ----------------------------
ALTER TABLE "public"."Receiver" ADD CONSTRAINT "_copy_14" PRIMARY KEY ("ci_person");

-- ----------------------------
-- Uniques structure for table Reception
-- ----------------------------
ALTER TABLE "public"."Reception" ADD CONSTRAINT "u_voucher" UNIQUE ("voucher");
ALTER TABLE "public"."Reception" ADD CONSTRAINT "u_id_reception" UNIQUE ("id");

-- ----------------------------
-- Primary Key structure for table Reception
-- ----------------------------
ALTER TABLE "public"."Reception" ADD CONSTRAINT "_copy_6" PRIMARY KEY ("id", "code_provider");

-- ----------------------------
-- Triggers structure for table Reception_Inventory
-- ----------------------------
CREATE TRIGGER "tr_add_product_from_provider_to_warehouse" AFTER INSERT ON "public"."Reception_Inventory"
FOR EACH ROW
EXECUTE PROCEDURE "public"."fn_add_product_from_provider_to_warehouse"();

-- ----------------------------
-- Primary Key structure for table Reception_Inventory
-- ----------------------------
ALTER TABLE "public"."Reception_Inventory" ADD CONSTRAINT "Reception_Inventory_pkey" PRIMARY KEY ("id_reception", "code_product", "code_provider");

-- ----------------------------
-- Primary Key structure for table Store Manager
-- ----------------------------
ALTER TABLE "public"."Store Manager" ADD CONSTRAINT "_copy_15" PRIMARY KEY ("ci_person");

-- ----------------------------
-- Primary Key structure for table Unit
-- ----------------------------
ALTER TABLE "public"."Unit" ADD CONSTRAINT "Unit_pkey" PRIMARY KEY ("code");

-- ----------------------------
-- Primary Key structure for table Warehouse
-- ----------------------------
ALTER TABLE "public"."Warehouse" ADD CONSTRAINT "_copy_1" PRIMARY KEY ("number");

-- ----------------------------
-- Primary Key structure for table Warehouse_Inventory
-- ----------------------------
ALTER TABLE "public"."Warehouse_Inventory" ADD CONSTRAINT "_copy_9" PRIMARY KEY ("number_warehouse", "code_product", "code_provider");

-- ----------------------------
-- Foreign Keys structure for table Cost Center
-- ----------------------------
ALTER TABLE "public"."Cost Center" ADD CONSTRAINT "fk_Cost Center_Unit" FOREIGN KEY ("code_unit") REFERENCES "public"."Unit" ("code") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Cost_Center_Inventory
-- ----------------------------
ALTER TABLE "public"."Cost_Center_Inventory" ADD CONSTRAINT "fk_Cost_Center_Inventory_Cost_Center" FOREIGN KEY ("code_cost_center") REFERENCES "public"."Cost Center" ("code") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Cost_Center_Inventory" ADD CONSTRAINT "fk_Cost_Center_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "public"."Product" ("code", "code_provider") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Delivery
-- ----------------------------
ALTER TABLE "public"."Delivery" ADD CONSTRAINT "fk_Delivery_Cost_Center" FOREIGN KEY ("code_cost_center") REFERENCES "public"."Cost Center" ("code") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Delivery" ADD CONSTRAINT "fk_Delivery_Dispatcher" FOREIGN KEY ("ci_dispatcher") REFERENCES "public"."Dispatcher" ("ci_person") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Delivery" ADD CONSTRAINT "fk_Delivery_Receiver" FOREIGN KEY ("ci_receiver") REFERENCES "public"."Receiver" ("ci_person") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Delivery" ADD CONSTRAINT "fk_Delivery_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "public"."Warehouse" ("number") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Delivery_Inventory
-- ----------------------------
ALTER TABLE "public"."Delivery_Inventory" ADD CONSTRAINT "fk_Delivery_Inventory_Delivery" FOREIGN KEY ("id_delivery") REFERENCES "public"."Delivery" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Delivery_Inventory" ADD CONSTRAINT "fk_Delivery_Inventory_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "public"."Product" ("code", "code_provider") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Devolution
-- ----------------------------
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "fk_Devolution_Dispatcher" FOREIGN KEY ("ci_dispatcher") REFERENCES "public"."Dispatcher" ("ci_person") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "fk_Devolution_Provider" FOREIGN KEY ("code_provider") REFERENCES "public"."Provider" ("code") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "fk_Devolution_Receiver" FOREIGN KEY ("ci_receiver") REFERENCES "public"."Receiver" ("ci_person") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Devolution" ADD CONSTRAINT "fk_Devolution_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "public"."Warehouse" ("number") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Devolution_Inventory
-- ----------------------------
ALTER TABLE "public"."Devolution_Inventory" ADD CONSTRAINT "fk_Devolution_Inventory_Devolution" FOREIGN KEY ("id_devolution", "code_provider") REFERENCES "public"."Devolution" ("id", "code_provider") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Devolution_Inventory" ADD CONSTRAINT "fk_Devolution_Inventory_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "public"."Product" ("code", "code_provider") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Dispatcher
-- ----------------------------
ALTER TABLE "public"."Dispatcher" ADD CONSTRAINT "fk_Dispatcher_Person" FOREIGN KEY ("ci_person") REFERENCES "public"."Person" ("ci") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Product
-- ----------------------------
ALTER TABLE "public"."Product" ADD CONSTRAINT "fk_Product_Provider" FOREIGN KEY ("code_provider") REFERENCES "public"."Provider" ("code") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Receiver
-- ----------------------------
ALTER TABLE "public"."Receiver" ADD CONSTRAINT "fk_Receiver_Person" FOREIGN KEY ("ci_person") REFERENCES "public"."Person" ("ci") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Reception
-- ----------------------------
ALTER TABLE "public"."Reception" ADD CONSTRAINT "fk_Reception_Provider" FOREIGN KEY ("code_provider") REFERENCES "public"."Provider" ("code") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Reception" ADD CONSTRAINT "fk_Reception_Receiver" FOREIGN KEY ("ci_receiver") REFERENCES "public"."Receiver" ("ci_person") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Reception" ADD CONSTRAINT "fk_Reception_Store Manager" FOREIGN KEY ("ci_store_manager") REFERENCES "public"."Store Manager" ("ci_person") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Reception" ADD CONSTRAINT "fk_Reception_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "public"."Warehouse" ("number") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Reception_Inventory
-- ----------------------------
ALTER TABLE "public"."Reception_Inventory" ADD CONSTRAINT "fk_Reception_Inventory_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "public"."Product" ("code", "code_provider") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Reception_Inventory" ADD CONSTRAINT "fk_Reception_Inventory_Reception" FOREIGN KEY ("id_reception", "code_provider") REFERENCES "public"."Reception" ("id", "code_provider") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Store Manager
-- ----------------------------
ALTER TABLE "public"."Store Manager" ADD CONSTRAINT "fk_Store Manager_Person" FOREIGN KEY ("ci_person") REFERENCES "public"."Person" ("ci") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- ----------------------------
-- Foreign Keys structure for table Warehouse_Inventory
-- ----------------------------
ALTER TABLE "public"."Warehouse_Inventory" ADD CONSTRAINT "fk_Warehouse_Inventory_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "public"."Product" ("code", "code_provider") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "public"."Warehouse_Inventory" ADD CONSTRAINT "fk_Warehouse_Inventory_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "public"."Warehouse" ("number") ON DELETE NO ACTION ON UPDATE NO ACTION;
