# ``WKInternalsNotes/_WKFeature/name``

Feature の表示名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *name;
```

## Discussion
ラップしている `API::Feature` の `name()` を `NSString` に変換して返す。

## References
- [`_WKFeature.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.h#L34)
- [`_WKFeature.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L50)
- [`_WKFeature.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
