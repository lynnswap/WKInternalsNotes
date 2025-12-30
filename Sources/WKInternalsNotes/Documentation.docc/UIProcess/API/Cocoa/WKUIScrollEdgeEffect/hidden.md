# ``WKInternalsNotes/WKUIScrollEdgeEffect/hidden``

クライアント起因の表示/非表示フラグを `UIScrollEdgeEffect` に反映する。

## Objective-C Declaration
```objective-c
@property (nonatomic, getter=isHidden) BOOL hidden;
```

## Default Value
`_hiddenSources` が空で、`UIScrollEdgeEffect.hidden` の状態に従う。

## Discussion
getter は `_effect.hidden` を返す。setter は `Client` ソースで `_setHidden:fromSource:` を呼び、`_hiddenSources` を更新して `UIScrollEdgeEffect.hidden` を切り替える（必要に応じて KVO 通知）。

## References
- [`WKUIScrollEdgeEffect.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.h#L40)
- [`WKUIScrollEdgeEffect.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.mm#L89)
- [`WKUIScrollEdgeEffect.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.mm#L94)
- [`WKUIScrollEdgeEffect.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.mm#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
