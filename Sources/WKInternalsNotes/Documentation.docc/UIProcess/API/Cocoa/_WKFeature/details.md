# ``WKInternalsNotes/_WKFeature/details``

Feature の詳細説明を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *details;
```

## Discussion
ラップしている `API::Feature` の `details()` を `NSString` に変換して返す。

## References
- [`_WKFeature.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.h#L37)
- [`_WKFeature.mm#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L114)
- [`_WKFeature.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L116)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
