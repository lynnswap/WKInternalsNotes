# ``WKInternalsNotes/WKWindowFeatures/_fullscreenDisplay``

fullscreen 表示

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, readonly) NSNumber *_fullscreenDisplay WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
windowFeatures().fullscreen があれば NSNumber を返し、なければ `nil`。

## References
- [`WKWindowFeaturesPrivate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeaturesPrivate.h#L32)
- [`WKWindowFeatures.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeatures.mm#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
