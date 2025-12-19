# ``WKInternalsNotes/WKWindowFeatures/_hasAdditionalFeatures``

追加の window feature の有無

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _hasAdditionalFeatures WK_API_AVAILABLE(macos(14.2), ios(17.2));
```

## Discussion
windowFeatures().hasAdditionalFeatures を返す。

## References
- [`WKWindowFeaturesPrivate.h#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeaturesPrivate.h#L28)
- [`WKWindowFeatures.mm#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeatures.mm#L127)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
