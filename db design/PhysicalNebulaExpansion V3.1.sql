CREATE TABLE "Accountant" (
  "ci_person" int8 NOT NULL,
  CONSTRAINT "_copy_12" PRIMARY KEY ("ci_person")
);

CREATE TABLE "Cost Center" (
  "code" int2 NOT NULL,
  "name" char(50),
  "code_unit" char(15),
  CONSTRAINT "_copy_16" PRIMARY KEY ("code")
);

CREATE TABLE "Delivery" (
  "id" serial4,
  "voucher" serial4,
  "code_cost_center" int2 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_dispatcher" int8,
  CONSTRAINT "_copy_5" PRIMARY KEY ("id"),
  CONSTRAINT "u_voucher_copy_2" UNIQUE ("voucher")
);

CREATE TABLE "Devolution" (
  "id" serial4,
  "voucher" serial4,
  "code_cost_center" int2 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_dispatcher" int8,
  "ci_receiver" int8,
  CONSTRAINT "_copy_4" PRIMARY KEY ("id"),
  CONSTRAINT "u_voucher_copy_1" UNIQUE ("voucher")
);

CREATE TABLE "Dispatcher" (
  "ci_person" int8 NOT NULL,
  CONSTRAINT "_copy_10" PRIMARY KEY ("ci_person")
);

CREATE TABLE "Order" (
  "id" serial4,
  "date_stamp" date NOT NULL,
  "id_devolution" int4,
  "id_delivery" int4,
  "id_reception" int4,
  CONSTRAINT "_copy_3" PRIMARY KEY ("id"),
  CONSTRAINT "one_dev" UNIQUE ("id_devolution"),
  CONSTRAINT "one_del" UNIQUE ("id_delivery"),
  CONSTRAINT "one_rec" UNIQUE ("id_reception"),
  CONSTRAINT "exactly_one_from" CHECK (id_delivery IS NULL AND id_devolution IS NULL AND id_reception IS NOT NULL OR id_delivery IS NULL AND id_devolution IS NOT NULL AND id_reception IS NULL OR id_delivery IS NOT NULL AND id_devolution IS NULL AND id_reception IS NULL)
);

CREATE TABLE "Order_Inventory" (
  "id_order" int4 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL,
  CONSTRAINT "_copy_8" PRIMARY KEY ("id_order", "code_product", "code_provider")
);

CREATE TABLE "Person" (
  "ci" int8 NOT NULL,
  "name" char(50),
  "last_name1" char(50),
  "last_name2" char(50),
  CONSTRAINT "_copy_13" PRIMARY KEY ("ci")
);

CREATE TABLE "Product" (
  "code" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "account_sub1" int2,
  "account_sub2" int2,
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

CREATE TABLE "Receiver" (
  "ci_person" int8 NOT NULL,
  CONSTRAINT "_copy_14" PRIMARY KEY ("ci_person")
);

CREATE TABLE "Reception" (
  "id" serial4,
  "voucher" serial4,
  "bill_number" varchar(255) NOT NULL,
  "code_provider" int4 NOT NULL,
  "number_warehouse" int2 NOT NULL,
  "ci_receiver" int8,
  "ci_store_manager" int8,
  "ci_accountant" int8,
  CONSTRAINT "_copy_6" PRIMARY KEY ("id"),
  CONSTRAINT "u_voucher" UNIQUE ("voucher")
);

CREATE TABLE "Store Manager" (
  "ci_person" int8 NOT NULL,
  CONSTRAINT "_copy_15" PRIMARY KEY ("ci_person")
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

CREATE TABLE "Warehouse_Inventory" (
  "number_warehouse" int2 NOT NULL,
  "code_product" int8 NOT NULL,
  "code_provider" int4 NOT NULL,
  "quantity" float4 NOT NULL,
  CONSTRAINT "_copy_9" PRIMARY KEY ("number_warehouse", "code_product", "code_provider")
);

ALTER TABLE "Accountant" ADD CONSTRAINT "fk_Accountant_Person" FOREIGN KEY ("ci_person") REFERENCES "Person" ("ci");
ALTER TABLE "Cost Center" ADD CONSTRAINT "fk_Cost Center_Unit" FOREIGN KEY ("code_unit") REFERENCES "Unit" ("code");
ALTER TABLE "Delivery" ADD CONSTRAINT "fk_Delivery_Receiver" FOREIGN KEY ("ci_receiver") REFERENCES "Receiver" ("ci_person");
ALTER TABLE "Delivery" ADD CONSTRAINT "fk_Delivery_Dispatcher" FOREIGN KEY ("ci_dispatcher") REFERENCES "Dispatcher" ("ci_person");
ALTER TABLE "Delivery" ADD CONSTRAINT "fk_Delivery_Cost Center" FOREIGN KEY ("code_cost_center") REFERENCES "Cost Center" ("code");
ALTER TABLE "Delivery" ADD CONSTRAINT "fk_Delivery_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Devolution" ADD CONSTRAINT "fk_Devolution_Receiver" FOREIGN KEY ("ci_receiver") REFERENCES "Receiver" ("ci_person");
ALTER TABLE "Devolution" ADD CONSTRAINT "fk_Devolution_Dispatcher" FOREIGN KEY ("ci_dispatcher") REFERENCES "Dispatcher" ("ci_person");
ALTER TABLE "Devolution" ADD CONSTRAINT "fk_Devolution_Cost Center" FOREIGN KEY ("code_cost_center") REFERENCES "Cost Center" ("code");
ALTER TABLE "Devolution" ADD CONSTRAINT "fk_Devolution_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Dispatcher" ADD CONSTRAINT "fk_Dispatcher_Person" FOREIGN KEY ("ci_person") REFERENCES "Person" ("ci");
ALTER TABLE "Order" ADD CONSTRAINT "fk_Order_Devolution" FOREIGN KEY ("id_devolution") REFERENCES "Devolution" ("id");
ALTER TABLE "Order" ADD CONSTRAINT "fk_Order_Delivery" FOREIGN KEY ("id_delivery") REFERENCES "Delivery" ("id");
ALTER TABLE "Order" ADD CONSTRAINT "fk_Order_Reception" FOREIGN KEY ("id_reception") REFERENCES "Reception" ("id");
ALTER TABLE "Order_Inventory" ADD CONSTRAINT "fk_Order_Inventory_Order" FOREIGN KEY ("id_order") REFERENCES "Order" ("id");
ALTER TABLE "Order_Inventory" ADD CONSTRAINT "fk_Order_Inventory_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");
ALTER TABLE "Product" ADD CONSTRAINT "fk_Product_Provider" FOREIGN KEY ("code_provider") REFERENCES "Provider" ("code");
ALTER TABLE "Receiver" ADD CONSTRAINT "fk_Receiver_Person" FOREIGN KEY ("ci_person") REFERENCES "Person" ("ci");
ALTER TABLE "Reception" ADD CONSTRAINT "fk_Reception_Receiver" FOREIGN KEY ("ci_receiver") REFERENCES "Receiver" ("ci_person");
ALTER TABLE "Reception" ADD CONSTRAINT "fk_Reception_Store Manager" FOREIGN KEY ("ci_store_manager") REFERENCES "Store Manager" ("ci_person");
ALTER TABLE "Reception" ADD CONSTRAINT "fk_Reception_Accountant" FOREIGN KEY ("ci_accountant") REFERENCES "Accountant" ("ci_person");
ALTER TABLE "Reception" ADD CONSTRAINT "fk_Reception_Provider" FOREIGN KEY ("code_provider") REFERENCES "Provider" ("code");
ALTER TABLE "Reception" ADD CONSTRAINT "fk_Reception_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Store Manager" ADD CONSTRAINT "fk_Store Manager_Person" FOREIGN KEY ("ci_person") REFERENCES "Person" ("ci");
ALTER TABLE "Warehouse_Inventory" ADD CONSTRAINT "fk_Warehouse_Inventory_Warehouse" FOREIGN KEY ("number_warehouse") REFERENCES "Warehouse" ("number");
ALTER TABLE "Warehouse_Inventory" ADD CONSTRAINT "fk_Warehouse_Inventory_Product" FOREIGN KEY ("code_product", "code_provider") REFERENCES "Product" ("code", "code_provider");

