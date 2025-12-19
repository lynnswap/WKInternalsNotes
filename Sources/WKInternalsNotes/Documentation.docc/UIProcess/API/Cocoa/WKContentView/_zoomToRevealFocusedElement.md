# ``WKInternalsNotes/WKContentView/_zoomToRevealFocusedElement()``

フォーカス要素が見えるようにズーム/スクロールする。

## Objective-C Declaration
```objective-c
- (void)_zoomToRevealFocusedElement;
```

## Discussion
スクロール禁止や選択抑制中は何もしない。条件が整えば `_zoomToFocusRect:` を呼び、フォーカス要素の矩形・フォントサイズ・スケール条件を渡して調整する。

## References
- [`WKContentViewInteraction.h#L769`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L769)
- [`WKContentViewInteraction.mm#L2913`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2913)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
