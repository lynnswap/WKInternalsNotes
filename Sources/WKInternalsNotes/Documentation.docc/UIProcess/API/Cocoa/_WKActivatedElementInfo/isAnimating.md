# ``WKInternalsNotes/_WKActivatedElementInfo/isAnimating``

アニメーション中かどうかを返す（iOS）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isAnimating;
```

## Default Value
初期化時に渡された `isAnimating` の値。

## Discussion
初期化時に `_isAnimating` を設定し、getter で返す。

## References
- [`_WKActivatedElementInfo.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L55)
- [`_WKActivatedElementInfo.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L160)
- [`_WKActivatedElementInfo.mm#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L219)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
