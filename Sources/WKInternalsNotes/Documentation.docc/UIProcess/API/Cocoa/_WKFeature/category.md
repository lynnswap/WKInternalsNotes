# ``WKInternalsNotes/_WKFeature/category``

Feature のカテゴリを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebFeatureCategory category;
```

## Discussion
`API::FeatureCategory` を `WebFeatureCategory` に変換して返す。`None` / `Animation` / `CSS` / `DOM` / `Extensions` / `HTML` / `Javascript` / `Media` / `Networking` / `Privacy` / `Security` をそれぞれ対応する列挙値へマップする。

## References
- [`_WKFeature.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.h#L36)
- [`_WKFeature.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L79)
- [`_WKFeature.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L81)
- [`_WKFeature.mm#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L103)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
