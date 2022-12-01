class User < ApplicationRecord
  validates :email, :name, :cellphone, presence: true
  validates :email, uniqueness: true #format: { with: /\A[^@\s]+[a-zA-Z0-9_]+@unal\.edu\.co\z/},
  validates :cellphone, format: { with: /\A\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*\z/}, uniqueness: true

  belongs_to :trip, :optional => true
  #belongs_to :trip_creator
  has_one :trip_bucket
  has_many :vehicles, dependent: :destroy
  has_many :trips
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  def add_vehicle(v)
    self.vehicles << Vehicle.find_by(id: v.id)
  end

  def add_trip_to_history(trip)
    self.trips << Trip.find_by(id: trip.id)
  end
end
