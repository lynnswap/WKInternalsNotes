# ``WKInternalsNotes/_WKTextInputContext/boundingRect``

対象要素のバウンディング矩形を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect boundingRect;
```

## Discussion
内部の `ElementContext` が保持する `boundingRect` を返す。

## References
- [`_WKTextInputContext.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextInputContext.h#L33)
- [`_WKTextInputContext.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextInputContext.mm#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
