# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2022_11_17_071345) do
  create_table "line_items", charset: "utf8mb4", collation: "utf8mb4_0900_ai_ci", force: :cascade do |t|
    t.bigint "trip_id"
    t.bigint "trip_bucket_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "quantity", default: 1
    t.index ["trip_bucket_id"], name: "index_line_items_on_trip_bucket_id"
    t.index ["trip_id"], name: "index_line_items_on_trip_id"
  end

  create_table "trip_buckets", charset: "utf8mb4", collation: "utf8mb4_0900_ai_ci", force: :cascade do |t|
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "trip_creators", charset: "utf8mb4", collation: "utf8mb4_0900_ai_ci", force: :cascade do |t|
    t.bigint "trip_id"
    t.bigint "user_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["trip_id"], name: "index_trip_creators_on_trip_id"
    t.index ["user_id"], name: "index_trip_creators_on_user_id"
  end

  create_table "trips", charset: "utf8mb4", collation: "utf8mb4_0900_ai_ci", force: :cascade do |t|
    t.float "origin_lat"
    t.float "origin_lng"
    t.string "img_url"
    t.integer "status"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.float "destination_lat"
    t.float "destination_lng"
    t.text "route_suggested"
    t.string "route_origin"
    t.string "route_destination"
    t.bigint "user_id"
    t.bigint "trip_creator_id"
    t.bigint "vehicle_id"
    t.index ["trip_creator_id"], name: "index_trips_on_trip_creator_id"
    t.index ["user_id"], name: "index_trips_on_user_id"
    t.index ["vehicle_id"], name: "index_trips_on_vehicle_id"
  end

  create_table "users", charset: "utf8mb4", collation: "utf8mb4_0900_ai_ci", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "name"
    t.string "cellphone"
    t.bigint "trip_id"
    t.bigint "vehicle_id"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
    t.index ["trip_id"], name: "index_users_on_trip_id"
    t.index ["vehicle_id"], name: "index_users_on_vehicle_id"
  end

  create_table "vehicles", charset: "utf8mb4", collation: "utf8mb4_0900_ai_ci", force: :cascade do |t|
    t.string "plate"
    t.bigint "user_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["user_id"], name: "index_vehicles_on_user_id"
  end

  add_foreign_key "line_items", "trip_buckets"
  add_foreign_key "line_items", "trips"
  add_foreign_key "trip_creators", "trips"
  add_foreign_key "trip_creators", "users"
  add_foreign_key "trips", "trip_creators"
  add_foreign_key "trips", "users"
  add_foreign_key "trips", "vehicles"
  add_foreign_key "users", "trips"
  add_foreign_key "users", "vehicles"
  add_foreign_key "vehicles", "users"
end
