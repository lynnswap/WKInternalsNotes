# ``WKInternalsNotes/_WKFeature/key``

Feature を識別するキーを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *key;
```

## Discussion
ラップしている `API::Feature` の `key()` を `NSString` に変換して返す。

## References
- [`_WKFeature.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.h#L33)
- [`_WKFeature.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L109)
- [`_WKFeature.mm#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
