CREATE TABLE "Adjust_Cancel" (
  "id_cancel_adjust" serial4,
  "id_adjust" int4,
  "date_stamp" date,
  "reason" varchar(255),
  "ci_store_manager" int8,
  "number_warehouse" int2,
  PRIMARY KEY ("id_cancel_adjust")
);

CREATE TABLE "Adjust_SC_2_16" (
  "id" serial4,
  "voucher" serial2,
  "date_stamp" date DEFAULT CURRENT_DATE,
  "concept" varchar(255),
  "number_warehouse" int2,
  "ci_store_manager" int8,
  "ci_inventory_manager" int8,
  PRIMARY KEY ("id")
);

CREATE TABLE "Adjust_Sheet" (
  "id_adjust" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL,
  "existence" float4,
  PRIMARY KEY ("id_adjust", "code_product", "code_provider")
);

CREATE TABLE "Cost Center" (
  "code" int2 NOT NULL,
  "name" char(50),
  "code_unit" char(15),
  CONSTRAINT "_copy_16" PRIMARY KEY ("code")
);

CREATE TABLE "Cost_Center_Dispatcher" (
  "ci_cost_center_dispatcher" int8 NOT NULL,
  "code_cost_center" int2 NOT NULL,
  "signature" varchar,
  CONSTRAINT "_copy_10" PRIMARY KEY ("ci_cost_center_dispatcher", "code_cost_center")
);

CREATE TABLE "Cost_Center_Inventory" (
  "code_cost_center" int2 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4,
  PRIMARY KEY ("code_cost_center", "code_product", "code_provider")
);

CREATE TABLE "Cost_Center_Receiver" (
  "ci_cost_center_receiver" int8 NOT NULL,
  "code_cost_center" int2 NOT NULL,
  "signature" varchar,
  PRIMARY KEY ("ci_cost_center_receiver", "code_cost_center")
);

CREATE TABLE "Cost_Center_Worker" (
  "ci_cost_center_worker" int8 NOT NULL,
  "code_cost_center" int2 NOT NULL,
  "name" varchar(50),
  "last_name1" varchar(50),
  "last_name2" varchar(50),
  "contract" date,
  "contract_expire" date,
  PRIMARY KEY ("ci_cost_center_worker", "code_cost_center"),
  CONSTRAINT "u_ci_cost_center_worker" UNIQUE ("ci_cost_center_worker")
);

CREATE TABLE "Delivery_Cancel" (
  "id_cancel_delivery" serial4,
  "id_delivery" int4,
  "date_stamp" date,
  "reason" varchar(255),
  "ci_store_manager" int8,
  "number_warehouse" int2,
  PRIMARY KEY ("id_cancel_delivery")
);

CREATE TABLE "Delivery_SC_2_08" (
  "id" serial4,
  "voucher" serial2,
  "request_voucher_1" int2,
  "request_voucher_2" int2,
  "request_plan" int2,
  "date_stamp" date NOT NULL DEFAULT CURRENT_DATE,
  "code_cost_center" int2 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_dispatcher" int8,
  CONSTRAINT "_copy_5" PRIMARY KEY ("id"),
  CONSTRAINT "different_responsable2" CHECK (ci_receiver <> ci_dispatcher)
);

CREATE TABLE "Delivery_Sheet" (
  "id_delivery" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL,
  "existence" float4,
  PRIMARY KEY ("id_delivery", "code_product", "code_provider")
);

CREATE TABLE "Devolution_Cancel" (
  "id_cancel_devolution" serial4,
  "id_devolution" int4,
  "date_stamp" date,
  "reason" varchar(255),
  "ci_store_manager" int8,
  "number_warehouse" int2,
  PRIMARY KEY ("id_cancel_devolution")
);

CREATE TABLE "Devolution_SC_2_08" (
  "id" serial4,
  "voucher" serial2,
  "date_stamp" date NOT NULL DEFAULT CURRENT_DATE,
  "code_cost_center" int2,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_dispatcher" int8,
  CONSTRAINT "_copy_4" PRIMARY KEY ("id"),
  CONSTRAINT "different_responsable1" CHECK (ci_receiver <> ci_dispatcher)
);

CREATE TABLE "Devolution_Sheet" (
  "id_devolution" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL,
  "existence" float4,
  PRIMARY KEY ("id_devolution", "code_product", "code_provider")
);

CREATE TABLE "Inventory_Manager" (
  "ci_inventory_manager" int8 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "signature" varchar,
  PRIMARY KEY ("ci_inventory_manager", "number_warehouse")
);

CREATE TABLE "Product" (
  "code" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "account" int2,
  "account_sub" int2,
  "description" char(50),
  "unit" char(10),
  "price" numeric(10,2) NOT NULL,
  CONSTRAINT "_copy_2" PRIMARY KEY ("code", "code_provider")
);

CREATE TABLE "Provider" (
  "code" int4 NOT NULL,
  "name" char(50),
  CONSTRAINT "_copy_11" PRIMARY KEY ("code")
);

CREATE TABLE "Reception_Cancel" (
  "id_cancel_reception" serial4,
  "id_reception" int4,
  "code_provider" int4,
  "date_stamp" date,
  "reason" varchar(255),
  "ci_store_manager" int8,
  "number_warehouse" int2,
  PRIMARY KEY ("id_cancel_reception")
);

CREATE TABLE "Reception_SC_2_04" (
  "id" serial4,
  "code_provider" int4 NOT NULL,
  "voucher" serial2,
  "date_stamp" date NOT NULL DEFAULT CURRENT_DATE,
  "bill_number" varchar(255) NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_store_manager" int8,
  CONSTRAINT "_copy_6" PRIMARY KEY ("id", "code_provider"),
  CONSTRAINT "u_id_reception" UNIQUE ("id")
);

CREATE TABLE "Reception_Sheet" (
  "id_reception" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL,
  "existence" float4,
  PRIMARY KEY ("id_reception", "code_product", "code_provider")
);

CREATE TABLE "Store_Manager" (
  "ci_store_manager" int8 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "signature" varchar,
  CONSTRAINT "_copy_15" PRIMARY KEY ("ci_store_manager", "number_warehouse")
);

CREATE TABLE "Unit" (
  "code" char(15) NOT NULL,
  "name" char(50),
  PRIMARY KEY ("code")
);

CREATE TABLE "Warehouse" (
  "number" int2 NOT NULL,
  "name" char(50),
  CONSTRAINT "_copy_1" PRIMARY KEY ("number")
);

CREATE TABLE "Warehouse_Dispatcher" (
  "ci_warehouse_dispatcher" int8 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "signature" varchar,
  PRIMARY KEY ("ci_warehouse_dispatcher", "number_warehouse")
);

CREATE TABLE "Warehouse_Inventory" (
  "number_warehouse" int2 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL,
  CONSTRAINT "_copy_9" PRIMARY KEY ("number_warehouse", "code_product", "code_provider")
);

CREATE TABLE "Warehouse_Receiver" (
  "ci_warehouse_receiver" int8 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "signature" varchar,
  CONSTRAINT "_copy_14" PRIMARY KEY ("ci_warehouse_receiver", "number_warehouse")
);

CREATE TABLE "Warehouse_Worker" (
  "ci_warehouse_worker" int8 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "name" varchar(50),
  "last_name1" varchar(50),
  "last_name2" varchar(50),
  "contract" date,
  "contract_expire" date,
  PRIMARY KEY ("ci_warehouse_worker", "number_warehouse"),
  CONSTRAINT "u_ci_warehouse_worker" UNIQUE ("ci_warehouse_worker")
);

ALTER TABLE "Adjust_Cancel" ADD CONSTRAINT "fk_Adjust_Cancel_SC_2_16" FOREIGN KEY ("id_adjust") REFERENCES "Adjust_SC_2_16" ("id");
ALTER TABLE "Adjust_Cancel" ADD CONSTRAINT "fk_Adjust_Cancel_Store_Manager" FOREIGN KEY ("ci_store_manager", "number_warehouse") REFERENCES "Store_Manager" ("ci_store_manager", "number_warehouse");
ALTER TABLE "Adjust_SC_2_16" ADD CONSTRAINT "fk_Adjust_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Adjust_SC_2_16" ADD CONSTRAINT "fk_Adjust_Store_Manager" FOREIGN KEY ("number_warehouse", "ci_store_manager") REFERENCES "Store_Manager" ("number_warehouse", "ci_store_manager");
ALTER TABLE "Adjust_SC_2_16" ADD CONSTRAINT "fk_Adjust_Inventory_Manager" FOREIGN KEY ("number_warehouse", "ci_inventory_manager") REFERENCES "Inventory_Manager" ("number_warehouse", "ci_inventory_manager");
ALTER TABLE "Adjust_Sheet" ADD CONSTRAINT "fk_Adjust_Sheet_SC_2_16" FOREIGN KEY ("id_adjust") REFERENCES "Adjust_SC_2_16" ("id");
ALTER TABLE "Adjust_Sheet" ADD CONSTRAINT "fk_Adjust_Sheet_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");
ALTER TABLE "Cost Center" ADD CONSTRAINT "fk_Cost Center_Unit" FOREIGN KEY ("code_unit") REFERENCES "Unit" ("code");
ALTER TABLE "Cost_Center_Dispatcher" ADD CONSTRAINT "fk_Cost_Center_Dispatcher_Cost_Center_Worker" FOREIGN KEY ("ci_cost_center_dispatcher", "code_cost_center") REFERENCES "Cost_Center_Worker" ("ci_cost_center_worker", "code_cost_center");
ALTER TABLE "Cost_Center_Inventory" ADD CONSTRAINT "fk_Cost_Center_Inventory_Cost_Center" FOREIGN KEY ("code_cost_center") REFERENCES "Cost Center" ("code");
ALTER TABLE "Cost_Center_Inventory" ADD CONSTRAINT "fk_Cost_Center_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");
ALTER TABLE "Cost_Center_Receiver" ADD CONSTRAINT "fk_Cost_Center_Receiver_Cost_Center_Worker" FOREIGN KEY ("ci_cost_center_receiver", "code_cost_center") REFERENCES "Cost_Center_Worker" ("ci_cost_center_worker", "code_cost_center");
ALTER TABLE "Cost_Center_Worker" ADD CONSTRAINT "fk_Cost_Center_Worker_Cost_Center" FOREIGN KEY ("code_cost_center") REFERENCES "Cost Center" ("code");
ALTER TABLE "Delivery_Cancel" ADD CONSTRAINT "fk_Delivery_Cancel_SC_2_08" FOREIGN KEY ("id_delivery") REFERENCES "Delivery_SC_2_08" ("id");
ALTER TABLE "Delivery_Cancel" ADD CONSTRAINT "fk_Delivery_Cancel_Store_Manager" FOREIGN KEY ("ci_store_manager", "number_warehouse") REFERENCES "Store_Manager" ("ci_store_manager", "number_warehouse");
ALTER TABLE "Delivery_SC_2_08" ADD CONSTRAINT "fk_Delivery_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Delivery_SC_2_08" ADD CONSTRAINT "fk_Delivery_Cost_Center" FOREIGN KEY ("code_cost_center") REFERENCES "Cost Center" ("code");
ALTER TABLE "Delivery_SC_2_08" ADD CONSTRAINT "fk_Delivery_Cost_Center_Receiver" FOREIGN KEY ("code_cost_center", "ci_receiver") REFERENCES "Cost_Center_Receiver" ("code_cost_center", "ci_cost_center_receiver");
ALTER TABLE "Delivery_SC_2_08" ADD CONSTRAINT "fk_Delivery_Warehouse_Dispatcher" FOREIGN KEY ("number_warehouse", "ci_dispatcher") REFERENCES "Warehouse_Dispatcher" ("number_warehouse", "ci_warehouse_dispatcher");
ALTER TABLE "Delivery_Sheet" ADD CONSTRAINT "fk_Delivery_Sheet_SC_2_08" FOREIGN KEY ("id_delivery") REFERENCES "Delivery_SC_2_08" ("id");
ALTER TABLE "Delivery_Sheet" ADD CONSTRAINT "fk_Delivery_Sheet_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");
ALTER TABLE "Devolution_Cancel" ADD CONSTRAINT "fk_Devolution_Cancel_SC_2_08" FOREIGN KEY ("id_devolution") REFERENCES "Devolution_SC_2_08" ("id");
ALTER TABLE "Devolution_Cancel" ADD CONSTRAINT "fk_Devolution_Cancel_Store_Manager" FOREIGN KEY ("ci_store_manager", "number_warehouse") REFERENCES "Store_Manager" ("ci_store_manager", "number_warehouse");
ALTER TABLE "Devolution_SC_2_08" ADD CONSTRAINT "fk_Devolution_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Devolution_SC_2_08" ADD CONSTRAINT "fk_Devolution_Cost_Center" FOREIGN KEY ("code_cost_center") REFERENCES "Cost Center" ("code");
ALTER TABLE "Devolution_SC_2_08" ADD CONSTRAINT "fk_Devolution_Warehouse_Receiver" FOREIGN KEY ("number_warehouse", "ci_receiver") REFERENCES "Warehouse_Receiver" ("number_warehouse", "ci_warehouse_receiver");
ALTER TABLE "Devolution_SC_2_08" ADD CONSTRAINT "fk_Devolution_Cost_Center_Dispatcher" FOREIGN KEY ("ci_dispatcher", "code_cost_center") REFERENCES "Cost_Center_Dispatcher" ("ci_cost_center_dispatcher", "code_cost_center");
ALTER TABLE "Devolution_Sheet" ADD CONSTRAINT "fk_Devolution_Sheet_SC_2_08" FOREIGN KEY ("id_devolution") REFERENCES "Devolution_SC_2_08" ("id");
ALTER TABLE "Devolution_Sheet" ADD CONSTRAINT "fk_Devolution_Sheet_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");
ALTER TABLE "Inventory_Manager" ADD CONSTRAINT "fk_Inventory_Manager_Warehouse_Worker" FOREIGN KEY ("ci_inventory_manager", "number_warehouse") REFERENCES "Warehouse_Worker" ("ci_warehouse_worker", "number_warehouse");
ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_Provider" FOREIGN KEY ("code_provider") REFERENCES "Provider" ("code");
ALTER TABLE "Reception_Cancel" ADD CONSTRAINT "fk_Reception_Cancel_SC_2_04" FOREIGN KEY ("id_reception", "code_provider") REFERENCES "Reception_SC_2_04" ("id", "code_provider");
ALTER TABLE "Reception_Cancel" ADD CONSTRAINT "fk_Reception_Cancel_Store_Manager" FOREIGN KEY ("ci_store_manager", "number_warehouse") REFERENCES "Store_Manager" ("ci_store_manager", "number_warehouse");
ALTER TABLE "Reception_SC_2_04" ADD CONSTRAINT "fk_Reception_Provider" FOREIGN KEY ("code_provider") REFERENCES "Provider" ("code");
ALTER TABLE "Reception_SC_2_04" ADD CONSTRAINT "fk_Reception_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Reception_SC_2_04" ADD CONSTRAINT "fk_Reception_Store_manager" FOREIGN KEY ("ci_store_manager", "number_warehouse") REFERENCES "Store_Manager" ("ci_store_manager", "number_warehouse");
ALTER TABLE "Reception_SC_2_04" ADD CONSTRAINT "fk_Reception_Warehouse_Receiver" FOREIGN KEY ("ci_receiver", "number_warehouse") REFERENCES "Warehouse_Receiver" ("ci_warehouse_receiver", "number_warehouse");
ALTER TABLE "Reception_Sheet" ADD CONSTRAINT "fk_Reception_Sheet_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");
ALTER TABLE "Reception_Sheet" ADD CONSTRAINT "fk_Reception_Sheet_SC_2_04" FOREIGN KEY ("id_reception", "code_provider") REFERENCES "Reception_SC_2_04" ("id", "code_provider");
ALTER TABLE "Store_Manager" ADD CONSTRAINT "fk_Store_Manager_Warehouse_Worker" FOREIGN KEY ("ci_store_manager", "number_warehouse") REFERENCES "Warehouse_Worker" ("ci_warehouse_worker", "number_warehouse");
ALTER TABLE "Warehouse_Dispatcher" ADD CONSTRAINT "fk_Warehouse_Dispatcher_Warehouse_Worker" FOREIGN KEY ("ci_warehouse_dispatcher", "number_warehouse") REFERENCES "Warehouse_Worker" ("ci_warehouse_worker", "number_warehouse");
ALTER TABLE "Warehouse_Inventory" ADD CONSTRAINT "fk_Warehouse_Inventory_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Warehouse_Inventory" ADD CONSTRAINT "fk_Warehouse_Inventory_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");
ALTER TABLE "Warehouse_Receiver" ADD CONSTRAINT "fk_Warehouse_Receiver_Warehouse_Worker" FOREIGN KEY ("ci_warehouse_receiver", "number_warehouse") REFERENCES "Warehouse_Worker" ("ci_warehouse_worker", "number_warehouse");
ALTER TABLE "Warehouse_Worker" ADD CONSTRAINT "fk_Warehouse_Worker_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");

