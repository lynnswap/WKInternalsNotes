# ``WKInternalsNotes/WKPDFHUDView/handleMouseUp(_:)``

マウスアップを処理し、必要なら操作を実行する。

## Objective-C Declaration
```objective-c
- (BOOL)handleMouseUp:(NSEvent *)event;
```

## Discussion
押下中のコントロールがなければ `false` を返す。マウスアップ位置が同じコントロールならアクションを実行し、レイヤーの不透明度を戻して状態をリセットする。

## References
- [`WKPDFHUDView.mm#L211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.mm#L211)
- [`WKPDFHUDView.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.h#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
