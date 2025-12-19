# ``WKInternalsNotes/WKFileUploadPanel/delegate``

ファイルアップロードパネルの delegate を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKFileUploadPanelDelegate> delegate;
```

## Default Value
`nil`。

## Discussion
パネルの終了通知や管理状態確認などのコールバック先として利用される。

## References
- [`WKFileUploadPanel.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.h#L52)
- [`WKFileUploadPanel.mm#L431`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.mm#L431)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
