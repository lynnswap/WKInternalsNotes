# ``WKInternalsNotes/_WKActivatedElementInfo/boundingRect``

要素の境界矩形を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect boundingRect;
```

## Default Value
`CGRectZero`（初期化時に設定される）。

## Discussion
`InteractionInformationAtPosition` の `bounds` を保持し、その値を返す。

## References
- [`_WKActivatedElementInfo.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L48)
- [`_WKActivatedElementInfo.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
