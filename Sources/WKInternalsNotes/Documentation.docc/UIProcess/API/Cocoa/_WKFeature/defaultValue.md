# ``WKInternalsNotes/_WKFeature/defaultValue``

Feature のデフォルト有効状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL defaultValue;
```

## Discussion
ラップしている `API::Feature` の `defaultValue()` をそのまま返す。

## References
- [`_WKFeature.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.h#L38)
- [`_WKFeature.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L119)
- [`_WKFeature.mm#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L121)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
