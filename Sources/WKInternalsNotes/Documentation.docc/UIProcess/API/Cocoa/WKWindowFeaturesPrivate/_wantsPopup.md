# ``WKInternalsNotes/WKWindowFeatures/_wantsPopup``

popup を要求しているか

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _wantsPopup WK_API_AVAILABLE(macos(14.2), ios(17.2));
```

## Discussion
windowFeatures().wantsPopup() を返す。

## References
- [`WKWindowFeaturesPrivate.h#L27`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeaturesPrivate.h#L27)
- [`WKWindowFeatures.mm#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeatures.mm#L122)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
