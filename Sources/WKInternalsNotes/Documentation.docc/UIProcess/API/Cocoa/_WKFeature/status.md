# ``WKInternalsNotes/_WKFeature/status``

Feature の公開状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebFeatureStatus status;
```

## Discussion
`API::FeatureStatus` の値を `WebFeatureStatus` に変換して返す。`Embedder` / `Unstable` / `Internal` / `Developer` / `Testable` / `Preview` / `Stable` / `Mature` をそれぞれ対応する列挙値へマップする。

## References
- [`_WKFeature.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.h#L35)
- [`_WKFeature.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L55)
- [`_WKFeature.mm#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L57)
- [`_WKFeature.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L73)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
