# ``WKInternalsNotes/_WKActivatedElementInfo/type``

アクティブ要素の種別を示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKActivatedElementType type;
```

## Default Value
生成経路により `_WKActivatedElementTypeUnspecified` などが設定される。

## Discussion
`_initWithInteractionInformationAtPosition:` ではリンク/画像/添付の判定に基づき設定され、内部初期化子では引数 `type` をそのまま保持する。

## References
- [`_WKActivatedElementInfo.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L34)
- [`_WKActivatedElementInfo.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
