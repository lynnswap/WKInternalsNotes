# ``WKInternalsNotes/_WKGeolocationPosition/positionWithLocation(_:)``

`CLLocation` から geolocation 位置情報を生成する。

## Objective-C Declaration
```objective-c
+ (instancetype)positionWithLocation:(CLLocation *)location;
```

## Discussion
`location` が `nil` の場合は `nil` を返す。`WebGeolocationPosition::create` に `CLLocation` を渡して wrapper を作り、Objective-C 側のインスタンスとして返す。

## References
- [`_WKGeolocationPosition.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationPosition.h#L39)
- [`_WKGeolocationPosition.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationPosition.mm#L36)
- [`_WKGeolocationPosition.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationPosition.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
