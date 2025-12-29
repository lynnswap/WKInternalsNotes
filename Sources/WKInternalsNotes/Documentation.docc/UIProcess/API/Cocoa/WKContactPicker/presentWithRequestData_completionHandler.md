# ``WKInternalsNotes/WKContactPicker/presentWithRequestData(_:completionHandler:)``

連絡先選択 UI を表示し、選択結果を返す。

## Objective-C Declaration
```objective-c
- (void)presentWithRequestData:(const WebCore::ContactsRequestData&)requestData completionHandler:(WTF::CompletionHandler<void(std::optional<Vector<WebCore::ContactInfo>>&&)>&&)completionHandler;
```

## Discussion
`requestData` のプロパティと完了ハンドラを保存し、単一/複数選択に応じた `WKCNContactPickerDelegate` を構成する。`CNContactPickerViewController` を提示し、表示完了後に `contactPickerDidPresent:` を通知する。

## References
- [`WKContactPicker.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.h#L49)
- [`WKContactPicker.mm#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKContactPicker.mm#L155)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
