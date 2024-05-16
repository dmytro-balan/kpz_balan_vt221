class Subscription:
    def __init__(self, monthly_fee, minimum_period, channels):
        self.monthly_fee = monthly_fee
        self.minimum_period = minimum_period
        self.channels = channels


class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=10, minimum_period=1, channels=["Domestic channels"])


class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=15, minimum_period=3, channels=["Educational channels"])


class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__(monthly_fee=25, minimum_period=6, channels=["Premium channels"])


class WebSite:
    def purchase_subscription(self, subscription_type):
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            return None


class MobileApp:
    def purchase_subscription(self, subscription_type):
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            return None


class ManagerCall:
    def purchase_subscription(self, subscription_type):
        if subscription_type == "domestic":
            return DomesticSubscription()
        elif subscription_type == "educational":
            return EducationalSubscription()
        elif subscription_type == "premium":
            return PremiumSubscription()
        else:
            return None


def main():
    website = WebSite()
    mobile_app = MobileApp()
    manager_call = ManagerCall()

    domestic_subscription = website.purchase_subscription("domestic")
    educational_subscription = mobile_app.purchase_subscription("educational")
    premium_subscription = manager_call.purchase_subscription("premium")

    print("Domestic subscription:")
    print(f"Monthly fee: ${domestic_subscription.monthly_fee}")
    print(f"Minimum period: {domestic_subscription.minimum_period} months")
    print(f"Channels: {', '.join(domestic_subscription.channels)}")

    print("\nEducational subscription:")
    print(f"Monthly fee: ${educational_subscription.monthly_fee}")
    print(f"Minimum period: {educational_subscription.minimum_period} months")
    print(f"Channels: {', '.join(educational_subscription.channels)}")

    print("\nPremium subscription:")
    print(f"Monthly fee: ${premium_subscription.monthly_fee}")
    print(f"Minimum period: {premium_subscription.minimum_period} months")
    print(f"Channels: {', '.join(premium_subscription.channels)}")


if __name__ == "__main__":
    main()
