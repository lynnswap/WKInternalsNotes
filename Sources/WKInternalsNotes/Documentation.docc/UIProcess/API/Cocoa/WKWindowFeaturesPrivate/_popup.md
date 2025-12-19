# ``WKInternalsNotes/WKWindowFeatures/_popup``

popup 指定

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, readonly) NSNumber *_popup WK_API_AVAILABLE(macos(14.2), ios(17.2));
```

## Discussion
windowFeatures().popup があれば NSNumber を返し、なければ `nil`。

## References
- [`WKWindowFeaturesPrivate.h#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeaturesPrivate.h#L29)
- [`WKWindowFeatures.mm#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeatures.mm#L132)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
