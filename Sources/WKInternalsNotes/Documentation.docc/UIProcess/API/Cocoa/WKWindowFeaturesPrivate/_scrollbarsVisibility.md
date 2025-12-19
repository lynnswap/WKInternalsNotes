# ``WKInternalsNotes/WKWindowFeatures/_scrollbarsVisibility``

scrollbar の可視性

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, readonly) NSNumber *_scrollbarsVisibility WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
windowFeatures().scrollbarsVisible があれば NSNumber を返し、なければ `nil`。

## References
- [`WKWindowFeaturesPrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeaturesPrivate.h#L36)
- [`WKWindowFeatures.mm#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWindowFeatures.mm#L148)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
