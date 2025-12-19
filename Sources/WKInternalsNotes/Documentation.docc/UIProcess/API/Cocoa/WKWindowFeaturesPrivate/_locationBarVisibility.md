# ``WKInternalsNotes/WKWindowFeatures/_locationBarVisibility``

location bar の可視性

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, readonly) NSNumber *_locationBarVisibility WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
windowFeatures().locationBarVisible があれば NSNumber を返し、なければ `nil`。

## References
- [`WKWindowFeaturesPrivate.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeaturesPrivate.h#L30)
- [`WKWindowFeatures.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeatures.mm#L140)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
