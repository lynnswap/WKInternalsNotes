# ``WKInternalsNotes/WKPDFHUDView/initWithFrame(_:pluginIdentifier:frameIdentifier:page:)``

PDF HUD を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithFrame:(NSRect)frame pluginIdentifier:(WebKit::PDFPluginIdentifier)pluginIdentifier frameIdentifier:(WebCore::FrameIdentifier)frameID page:(WebKit::WebPageProxy&)page;
```

## Discussion
レイヤーを有効化し、アイコンキャッシュや識別子、`WebPageProxy` を保持する。`deviceScaleFactor` を取得してレイヤーを構築し、一定時間後に非表示へ移行するタイマーを開始する。

## References
- [`WKPDFHUDView.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.mm#L106)
- [`WKPDFHUDView.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/PDF/WKPDFHUDView.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
