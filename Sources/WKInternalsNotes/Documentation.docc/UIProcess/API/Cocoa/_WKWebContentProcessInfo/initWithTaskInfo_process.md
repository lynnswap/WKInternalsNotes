# ``WKInternalsNotes/_WKWebContentProcessInfo/initWithTaskInfo(_:process:)``

TaskInfo と WebProcessProxy からプロセス情報を構築する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithTaskInfo:(const WebKit::AuxiliaryProcessProxy::TaskInfo&)info process:(const WebKit::WebProcessProxy&)process;
```

## Discussion
`_WKProcessInfo` の `initWithTaskInfo:` を呼んだ後、プロセスの状態に応じて `webContentState` を決定し、アクティブ時のみ `process.pages()` の `cocoaView()` を収集する。加えて ServiceWorker/SharedWorker の稼働有無と各状態の累積時間を取り込む。

## References
- [`WKProcessPool.mm#L796`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L796)
- [`WKProcessPool.mm#L801`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L801)
- [`WKProcessPool.mm#L807`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L807)
- [`WKProcessPool.mm#L817`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L817)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
