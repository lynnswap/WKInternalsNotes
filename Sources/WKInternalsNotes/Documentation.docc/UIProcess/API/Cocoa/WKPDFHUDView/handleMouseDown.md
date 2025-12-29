# ``WKInternalsNotes/WKPDFHUDView/handleMouseDown(_:)``

マウスダウンを処理し、押下状態を反映する。

## Objective-C Declaration
```objective-c
- (BOOL)handleMouseDown:(NSEvent *)event;
```

## Discussion
イベント位置から対象コントロールを特定し、セパレータの場合は無視する。コントロールがあれば対応レイヤーの不透明度を下げて押下状態を表示し、`true` を返す。

## References
- [`WKPDFHUDView.mm#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.mm#L190)
- [`WKPDFHUDView.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.h#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
