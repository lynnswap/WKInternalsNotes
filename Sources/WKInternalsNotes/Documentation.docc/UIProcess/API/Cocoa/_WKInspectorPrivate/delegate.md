# ``WKInternalsNotes/_WKInspector/delegate``

インスペクタのイベント通知先を設定し、外部 URL オープン要求やフロントエンド読み込み完了の通知を受け取れるようにする。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <_WKInspectorDelegate> delegate WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
`nil`

## Discussion
`setDelegate:` は `_WKInspector` が保持する弱参照の delegate を更新し、`InspectorClient` を差し替えて通知経路を設定する。`InspectorClient` は `respondsToSelector:` を使って実装の有無を判定し、対応している場合のみ delegate に転送するため、`nil` の場合は通知されない。

## References
- [`_WKInspector.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L43)
- [`_WKInspectorInternal.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorInternal.h#L46)
- [`_WKInspector.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L56)
- [`_WKInspector.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
