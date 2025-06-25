pipeline {
	agent any
	environment {
		WEBHOOK_NISHBOX = credentials("webhook-nishbox")
		WEBHOOK_ORIN = credentials("webhook-orin")
		WEBHOOK_PRIVATE1 = credentials("webhook-private1")
	}
	stages {
		stage("Build"){
			parallel {
				stage("MSVC Build for 32-bit") {
					agent {
						label "2012r2"
					}
					steps {
						bat "git submodule update --init --recursive"
						dir("nishbox") {
							bat "premake5 vs2015 --engine=dynamic --opengl=gdi --cc=msc --prefix=C:/Games"
							bat "msbuild nishbox.sln /p:Configuration=Release"
							bat "pack -d data base.pak"
						}
						dir("nsis") {
							bat "makensis /DCONFIG=Release /DPLATFORM=Native install.nsi"
							bat "move /y install.exe ..\\install32-vs2015.exe"
						}
						archiveArtifacts(
							"install32-vs2015.exe"
						)
					}
					post {
						always {
							post_always(false, false)
						}
					}
				}
				stage("Build for Windows 64-bit") {
					agent any
					steps {
						sh "git submodule update --init --recursive"
						dir("nishbox") {
							sh "premake5 gmake --engine=dynamic --opengl=gdi --prefix=C:/Games"
							sh "gmake config=release_win64 -j9"
							sh "pack -d data base.pak"
							sh "./tool/pack.sh Win64 nishbox ../nishbox64.zip"
						}
						dir("nsis") {
							sh "makensis -DCONFIG=Release -DPLATFORM=Win64 install.nsi"
							sh "mv install.exe ../install64.exe"
						}
						archiveArtifacts(
							"nishbox64.zip, install64.exe"
						)
					}
					post {
						always {
							post_always(false, false)
						}
					}
				}
				stage("Build for Windows 32-bit") {
					agent any
					steps {
						sh "git submodule update --init --recursive"
						dir("nishbox") {
							sh "premake5 gmake --engine=dynamic --opengl=gdi --prefix=C:/Games"
							sh "gmake config=release_win32 -j9"
							sh "pack -d data base.pak"
							sh "./tool/pack.sh Win32 nishbox ../nishbox32.zip"
						}
						dir("nsis") {
							sh "makensis -DCONFIG=Release -DPLATFORM=Win32 install.nsi"
							sh "mv install.exe ../install32.exe"
						}
						archiveArtifacts(
							"nishbox32.zip, install32.exe"
						)
					}
					post {
						always {
							post_always(false, false)
						}
					}
				}
			}
			post {
				always {
					post_always(true, true, true)
				}
			}
		}
	}
}

def post_always(cmt,art,alw=false){
	def list = [env.WEBHOOK_NISHBOX, env.WEBHOOK_ORIN, env.WEBHOOK_PRIVATE1]
	for(int i = 0; i < list.size(); i++){
		if(alw || currentBuild.currentResult != "SUCCESS"){
			discordSend(
				webhookURL: list[i],
				link: env.BUILD_URL,
				result: currentBuild.currentResult,
				title: "${env.JOB_NAME} - ${env.STAGE_NAME}",
				showChangeset: cmt,
				enableArtifactsList: art,
				description: "**Build:** ${env.BUILD_NUMBER}\n**Status:** ${currentBuild.currentResult}"
			)
		}
	}
}
