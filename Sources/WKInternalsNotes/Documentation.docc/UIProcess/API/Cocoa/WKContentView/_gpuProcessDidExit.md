# ``WKInternalsNotes/WKContentView/_gpuProcessDidExit()``

GPU プロセス終了時の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_gpuProcessDidExit;
```

## Discussion
可視性伝播ビューを GPU プロセスから切り離す。

## References
- [`WKContentView.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L100)
- [`WKContentView.mm#L916`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L916)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
