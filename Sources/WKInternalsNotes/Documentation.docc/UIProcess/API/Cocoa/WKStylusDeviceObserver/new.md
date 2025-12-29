# ``WKInternalsNotes/WKStylusDeviceObserver/new()``

`new` による生成は不可。

## Objective-C Declaration
```objective-c
+ (instancetype)new NS_UNAVAILABLE;
```

## Discussion
`NS_UNAVAILABLE` のため使用できず、`sharedInstance` を利用する。

## References
- [`WKStylusDeviceObserver.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.h#L31)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
