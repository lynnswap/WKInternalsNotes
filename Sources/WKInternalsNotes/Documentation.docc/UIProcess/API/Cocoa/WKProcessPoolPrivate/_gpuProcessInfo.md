# ``WKInternalsNotes/WKProcessPool/_gpuProcessInfo()``

GPU プロセスのタスク情報を `_WKProcessInfo` で返す。

## Objective-C Declaration
```objective-c
+ (_WKProcessInfo *)_gpuProcessInfo WK_API_AVAILABLE(macos(14.5));
```

## Discussion
GPUProcessProxy の `taskInfo()` が得られる場合に `_WKProcessInfo` を生成し、取得できない場合は `nil` を返す。

## References
- [`WKProcessPoolPrivate.h#L194`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L194)
- [`WKProcessPool.mm#L685`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L685)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
