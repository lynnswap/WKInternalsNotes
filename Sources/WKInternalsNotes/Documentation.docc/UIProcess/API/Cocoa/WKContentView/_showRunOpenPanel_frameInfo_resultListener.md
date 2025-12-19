# ``WKInternalsNotes/WKContentView/_showRunOpenPanel(_:frameInfo:resultListener:)``

ファイル選択用のオープンパネルを表示する。

## Objective-C Declaration
```objective-c
- (void)_showRunOpenPanel:(API::OpenPanelParameters*)parameters frameInfo:(const WebKit::FrameInfoData&)frameInfo resultListener:(WebKit::WebOpenPanelResultListenerProxy*)listener;
```

## Discussion
既存の `_fileUploadPanel` がある場合は何もしない。`_frameInfoForFileUploadPanel` を保存し、`WKFileUploadPanel` を生成して delegate を設定し、`presentWithParameters:resultListener:` で表示する。

## References
- [`WKContentViewInteraction.h#L829`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L829)
- [`WKContentViewInteraction.mm#L9680`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9680)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
