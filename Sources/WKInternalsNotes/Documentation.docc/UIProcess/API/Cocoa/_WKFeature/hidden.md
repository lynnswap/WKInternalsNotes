# ``WKInternalsNotes/_WKFeature/hidden``

Feature が非表示扱いかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isHidden) BOOL hidden;
```

## Discussion
ラップしている `API::Feature` の `isHidden()` をそのまま返す。

## References
- [`_WKFeature.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.h#L39)
- [`_WKFeature.mm#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L124)
- [`_WKFeature.mm#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFeature.mm#L126)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
